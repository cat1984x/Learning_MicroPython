//把编码器正交编码板OUTA信号连接到Arduino控制器的数字端口2，
//数字端口2是Arduino的外部中断0的端口。
#define PinA 2 //外部中断0
//把编码器正交编码板OUTB信号连接到Arduino控制器的数字端口3，
//数字端口3是Arduino的外部中断1的端口。
#define PinB 3  //外部中断1
int E1 =5; //L298P直流电机驱动板的电机使能端口连接到数字接口5
int M1 =4; //L298P直流电机驱动板的电机转向端口连接到数字接口4
//定义暂存数组，用于存储上位机发出的3个电机控制字节
//第一个字节用于控制电机是否启动；
//第二个字节用于控制电机是正转还是反转；
//第三个字节用于提供给电机PWM调数值。
byte val[3];
int count = 0;   //定义编码器码盘的计数值（此编码器转一圈发出12个脉冲）
int rpm = 0;    //定义每分钟(min)转速(r/min)
int  rpm_HIGH;  //定义转速rpm分解的两个高低字节
int  rpm_LOW;
byte flag;     //定义上传给上位机的用于判断电机正转还是反转的标志字节
unsigned long time = 0, old_time = 0; //时间标记
unsigned long time_delay = 0; // 时间标记
//初始化
void setup()
{
  Serial.begin(9600);    //启动串口通信，波特率9600b/s
  pinMode(M1, OUTPUT);   //L298P直流电机驱动板的控制端口设置为输出模式
   pinMode(E1, OUTPUT);
  pinMode(PinA,INPUT); //伺服电机正交编码板的OUTA和OUTB信号端设置为输入模式
  pinMode(PinB,INPUT);
  //定义外部中断0的中断子程序Code( ),中断触发为下跳沿触发
  //当编码器的正交编码板OUTA脉冲信号发生下跳沿中断时，
  //将自动调用执行中断子程序Code( )。
  attachInterrupt(0, Code, FALLING);
}
//主程序
void loop()
{
  if (Serial.available()>2) //如果Arduino控制板的读缓冲区中存在上位机下达的字节
  {
     for(int i=0; i<3; i++)//for循环次数与上位机下达的字节数一致
     {val[i] = Serial.read(); //读出Arduino控制板读缓冲区的字节
      delay(5); 
      }
     if(val[0]==0x11)        //如果读出的第一个字节为启动标志字节0x11
     {
       if(val[1]==0xAA)        //如果读出的第二个字节为正转标志字节0xAA
       {
         digitalWrite(M1,HIGH); //电机正转
         analogWrite(E1,val[2]); //电机以第三个字节中PWM调速值的转速转动         
         count = 0;
         old_time=  millis();   
       }
       else if(val[1]==0xBB)  //如果读出的第二个字节为反转标志字节0xBB  
       {
        digitalWrite(M1,LOW); //电机反转 
        analogWrite(E1,val[2]); //电机以第三个字节中PWM调速值的转速转动         
        count = 0;
        old_time=  millis();       
       }
     }
      else //如果读出的第一个字节不是启动标志字节0x11
      {
        digitalWrite(E1, LOW); //电机停止       
        count = 0;    
        old_time=  millis();        
      }
  }
  time = millis();//以毫秒为单位，计算当前时间
  //计算出每一秒钟编码器码盘计得的脉冲数，
  if(abs(time - old_time) >= 1000) //如果计时时间已达1秒
  {
    detachInterrupt(0); // 关闭外部中断0
    old_time= millis();  // 记录每次测速时的时间节点
     //把每一秒钟编码器码盘计得的脉冲数，换算为当前转速值
     //此编码器码盘为12个齿。
    rpm =(float)count*60/12;
    rpm_HIGH=rpm/256;//把转速值分解为高字节和低字节
    rpm_LOW=rpm%256;  
    Serial.print(flag,BYTE);    //向上位计算机上传电机转向标志字节
    Serial.print(rpm_HIGH,BYTE);//向上位计算机上传电机当前转速的高字节     
    Serial.print(rpm_LOW,BYTE); //向上位计算机上传电机当前转速的低字节 
    count = 0;   //把脉冲计数值清零，以便计算下一秒的脉冲计数        
    attachInterrupt(0, Code,FALLING); // 重新开放外部中断0
  }
}
 
// 编码器码盘计数中断子程序
void Code()
{
  //如果编码器的正交编码板OUTA脉冲信号下跳沿中断时，
  //正交编码板OUTA为低电平，则当前电机转向为正转。
  if(digitalRead(PinB)==LOW)
    {
      flag=0x7F;//电机当前转向为正转，则转向标志为0x7F
    }
   //如果编码器码盘的正交编码板OUTA脉冲信号下跳沿中断时，
  //正交编码板OUTA为高电平，则当前电机转向为反转。
   else
    {
     flag=0xFF; //电机当前转向为反转，则转向标志为0xFF
    }  
  //为了不计入噪音干扰脉冲，
   //当2次中断之间的时间大于5ms时，计一次有效计数
   if((millis()-time_delay) > 5)
  //当编码器正交编码板OUTA脉冲信号下跳沿每中断一次，
  count += 1; // 编码器码盘计数加一 
  time_delay=millis(); 
}
