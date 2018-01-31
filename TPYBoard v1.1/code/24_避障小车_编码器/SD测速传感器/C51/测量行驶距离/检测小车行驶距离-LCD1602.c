/******************************************************************************************
�����������С����ʹ����-LCD1602
��д�ˣ�Yayi
��̳��rtrobot.org������                                                
/******************************************************************************************/

#include <STC12C5A60S2.H>//ͷ�ļ�
#include <LCD1602.h>

sbit IN1=P1^0;
sbit IN2=P1^1;
sbit IN3=P1^2;
sbit IN4=P1^3;

unsigned int motor1=0;	 //��������������ֵ
unsigned int motor2=0;	 //���ҵ����������ֵ

void Forward(void)
{
        IN1=1;
        IN2=0;
        IN3=0;
        IN4=1;
}

/*********************************************************************************************
�ⲿ�ж�INT0��INT1��ʼ������
/********************************************************************************************/
void INT_init (void)
{
	EA = 1;			//�ж��ܿ���  
	EX0 = 1; 		//�����ⲿ�ж�0�ж�
	IT0 = 1; 		//1�����ش���  0���͵�ƽ����
	EX1 = 1;
	IT1	= 1;
}

/*********************************************************************************************
������
/********************************************************************************************/
void main(void)
{		
	LCD1602_Init();
	LCD1602_Frist();
	INT_init();
	Forward();
	while (1)
	{
		print(line_one,1,'M');
		print(line_one,2,'o');
		print(line_one,3,'t');
		print(line_one,4,'o');
		print(line_one,5,'r');
		print(line_one,6,'1');
		print(line_one,7,':');
		print(line_one,8,motor1/1000+0x30);
		print(line_one,9,motor1/100%10+0x30);
		print(line_one,10,motor1/10%10+0x30);
		print(line_one,11,motor1%10+0x30);
		print(line_one,12,'C');
		print(line_one,13,'M');

		print(line_two,1,'M');
		print(line_two,2,'o');
		print(line_two,3,'t');
		print(line_two,4,'o');
		print(line_two,5,'r');
		print(line_two,6,'2');
		print(line_two,7,':');
		print(line_two,8,motor2/1000+0x30);
		print(line_two,9,motor2/100%10+0x30);
		print(line_two,10,motor2/10%10+0x30);
		print(line_two,11,motor2%10+0x30);
		print(line_two,12,'C');
		print(line_two,13,'M');
		DELAY_MS(250);
		LCD1602_WriteCMD(CMD_clear);
		}
}

/*********************************************************************************************
�ⲿ�ж�INT0������1������
/********************************************************************************************/
void intersvr1(void) interrupt 0 using 1
{
	motor1++;	
	if(motor1>=9999)
		motor1=0;	
}
/*********************************************************************************************
�ⲿ�ж�INT1������2������
/********************************************************************************************/
void intersvr2(void) interrupt 2 using 3
{
	motor2++;
	if(motor2>=9999)
		motor2=0;
}