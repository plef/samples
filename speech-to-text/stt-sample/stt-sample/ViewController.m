//
//  ViewController.m
//  stt-sample
//
//  Created by Petr Lefner on 24.03.17.
//  Copyright © 2017 Petr Lefner. All rights reserved.
//

#import "ViewController.h"



@interface ViewController ()
{
    SFSpeechRecognizer*  m_stt;
    SFSpeechRecognitionTask* m_sttTask;
    SFSpeechAudioBufferRecognitionRequest* m_sttRequest;
    AVAudioEngine* m_audio;
}
@property (weak, nonatomic) IBOutlet UILabel *label;
@property (weak, nonatomic) IBOutlet UIButton *micBtn;
@property (weak, nonatomic) IBOutlet UITextView *textView;
- (IBAction)micBtnTapped:(id)sender;
- (void)updateTitles:(BOOL)toListenState;
- (void)startRecording;
- (void)speechRecognizer:(SFSpeechRecognizer *)speechRecognizer availabilityDidChange:(BOOL)available;
@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
    _micBtn.enabled = NO;
    _textView.text = @"";

    // Ask for permissions to mic - via speech recognzier
    [SFSpeechRecognizer requestAuthorization:^(SFSpeechRecognizerAuthorizationStatus status) {
        switch (status) {
            case SFSpeechRecognizerAuthorizationStatusAuthorized:
            {
                m_stt = [[SFSpeechRecognizer alloc] initWithLocale:[NSLocale localeWithLocaleIdentifier:@"en-US"]];
                m_stt.delegate = self;
                m_audio = [[AVAudioEngine alloc] init];
                [[NSRunLoop mainRunLoop] performBlock:^{
                    [self.micBtn setEnabled:YES];
                }];
            }
                break;
            case SFSpeechRecognizerAuthorizationStatusDenied:
            case SFSpeechRecognizerAuthorizationStatusRestricted:
            case SFSpeechRecognizerAuthorizationStatusNotDetermined:
            default:
                [self.label setText:@"Speech recognition was disabled for me."];
                break;
        }
    }];
}


- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


- (IBAction)micBtnTapped:(id)sender {
    if ([m_audio isRunning]) {
        [m_audio stop];
        [m_sttRequest endAudio];
        [self.micBtn setEnabled:NO];
        [self updateTitles:NO];
    } else {
        [self startRecording];
        [self updateTitles:YES];
    }
}

- (void)updateTitles:(BOOL)toListenState {
    if (toListenState) {
        [self.textView setText:@""];
        [self.label setText:@"Listening..."];
        [self.micBtn setTitle:@"Cancel" forState:UIControlStateNormal];
    } else {
        [self.label setText:@"Hello, what can I help you with?"];
        [self.micBtn setTitle:@"Start Recording" forState:UIControlStateNormal];
    }
}

# pragma mark -
# pragma mark SFSpeechRecognizerDelegate methods

- (void)speechRecognizer:(SFSpeechRecognizer *)speechRecognizer availabilityDidChange:(BOOL)available {
    [self.micBtn setEnabled:available];
}

# pragma mark -
# pragma mark Implementation

- (void)startRecording {
    if (m_sttTask != nil) {
        [m_sttTask cancel];
        m_sttTask = nil;
    }
    AVAudioSession * as = [AVAudioSession sharedInstance];
    NSError * error = nil;
    @try {
        [as setCategory:AVAudioSessionCategoryRecord error:&error];
        [as setMode:AVAudioSessionModeMeasurement error:&error];
        [as setActive:YES error:&error];
    }
    @catch (id) {
        NSLog(@"ERROR: audioSession properties weren't set because of an error.");
        return;
    }

    if ([m_audio inputNode] == nil) {
        NSLog(@"ERROR: Audio engine has no input node");
        return;
    }

    m_sttRequest = [[SFSpeechAudioBufferRecognitionRequest alloc] init];
    if (m_sttRequest == nil) {
        NSLog(@"ERROR: Unable to create an SFSpeechAudioBufferRecognitionRequest object");
        return;
    }

    m_sttRequest.shouldReportPartialResults = YES;
    m_sttTask = [m_stt recognitionTaskWithRequest:m_sttRequest resultHandler:^(SFSpeechRecognitionResult * _Nullable result, NSError * _Nullable error) {
        BOOL isFinal = YES;

        if (result != nil) {
            [self.textView setText:[[result bestTranscription] formattedString]];   // all what whas said so far
            isFinal = [result isFinal];
        }

        if (error != nil || isFinal) {
            [m_audio stop];
            [[m_audio inputNode] removeTapOnBus:0];

            m_sttRequest = nil;
            m_sttTask = nil;

            [self.micBtn setEnabled:YES];
            [self updateTitles:NO];
        }
    }];

    [[m_audio inputNode] installTapOnBus:0
                              bufferSize:1024
                                  format:[[m_audio inputNode] outputFormatForBus:0]
                                   block:^(AVAudioPCMBuffer * _Nonnull buffer, AVAudioTime * _Nonnull when) {
                                       [m_sttRequest appendAudioPCMBuffer:buffer];
    }];

    [m_audio prepare];
    @try {
        [m_audio startAndReturnError:&error];
    }
    @catch (id) {
        NSLog(@"audioEngine couldn't start because of an error.");
    }
}
@end
