#import "RootViewController.h"

@implementation RootViewController
- (void)loadView {
	self.view = [[[UIView alloc] initWithFrame:[[UIScreen mainScreen] applicationFrame]] autorelease];
	self.view.backgroundColor = [UIColor greenColor];

helloLabel = [[UILabel alloc] initWithFrame:CGRectMake(21,0,self.view.frame.size.width,44)];
helloLabel.text = @("SKUNKKKKKKKKK!!!!!");
helloLabel.backgroundColor = [UIColor clearColor];
helloLabel.textAlignment = UITextAlignmentLeft;
[self.view addSubview:helloLabel];
system("csay 'lick my anus'");
}
@end
