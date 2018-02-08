/**********  蓝牙智能小车 By 李成杰  ************/
            
int left_moto2 = 2;//left 左
int left_moto4 = 4;
int right_moto7 = 7;//right 右
int right_moto8 = 8;
int pwmleft=5; // pwm调速左
int pwmright=3; // pwm调速右
int RSpeed=175;
int BZQL;  //避障前左 13
int BZQR;  //避障前右 12
int BZL;  //避障左    11
int BZR;  //避障右    10
int pd=0;
int strat=0;

void setup()
{
  Serial.begin(57600);  //开启串口 波特率：115200
  
  /*      电机输出口    */
  pinMode(left_moto2,1);  //端口2输出
  pinMode(left_moto4,1);  
  pinMode(right_moto7,1); 
  pinMode(right_moto8,1);
  pinMode(pwmleft,1);
  pinMode(pwmright,1); 
 
   /*    红外壁障读取口    */ 
  pinMode(13,INPUT);    //端口13输入，红外传感器输入口
  pinMode(12,INPUT);
  pinMode(11,INPUT);
  pinMode(10,INPUT);
}
 
/*******************************    电机输出模式    *****************************/
void qian() //前进
{
  digitalWrite(right_moto7,1);  //数字端口7输出高电平
  digitalWrite(right_moto8,0);  
  digitalWrite(left_moto2,1);
  digitalWrite(left_moto4,0);
  analogWrite(pwmleft,255);
  analogWrite(pwmright,RSpeed);
}
void qianBZ() //前进
{
  digitalWrite(right_moto7,1);  //数字端口7输出高电平
  digitalWrite(right_moto8,0);  
  digitalWrite(left_moto2,1);
  digitalWrite(left_moto4,0);
  analogWrite(pwmleft,100);
  analogWrite(pwmright,75);
}
void hou()  //后退
{
  digitalWrite(right_moto7,0);
  digitalWrite(right_moto8,1);
  digitalWrite(left_moto2,0);
  digitalWrite(left_moto4,1);
  analogWrite(pwmleft,255);
  analogWrite(pwmright,RSpeed);
}
void houBZ()  //后退
{
  digitalWrite(right_moto7,0);
  digitalWrite(right_moto8,1);
  digitalWrite(left_moto2,0);
  digitalWrite(left_moto4,1);
  analogWrite(pwmleft,100);
  analogWrite(pwmright,75);
}
void zuo()  //左
 {
    digitalWrite(left_moto2,1);
    digitalWrite(left_moto4,0);
    digitalWrite(right_moto7,0);
    digitalWrite(right_moto8,0);
    analogWrite(pwmleft,0);
    analogWrite(pwmright,255);
 } 
void you() //右
 {
   digitalWrite(left_moto2,0);
   digitalWrite(left_moto4,0);
   digitalWrite(right_moto7,1);
   digitalWrite(right_moto8,0);
   analogWrite(pwmleft,255);
   analogWrite(pwmright,0);
 }
 void yuanzuo()//原地左转
 {
   digitalWrite(right_moto7,0);
   digitalWrite(right_moto8,1);
   digitalWrite(left_moto2,1);
   digitalWrite(left_moto4,0);
   analogWrite(pwmleft,80);
   analogWrite(pwmright,80);
 }
 void yuanyou() //原地右转
 {
   digitalWrite(right_moto7,1);
   digitalWrite(right_moto8,0);
   digitalWrite(left_moto2,0);
   digitalWrite(left_moto4,1);
   analogWrite(pwmleft,80);
   analogWrite(pwmright,80);
 }
  void yuanzuoBZ()//原地左转
 {
   digitalWrite(right_moto7,0);
   digitalWrite(right_moto8,1);
   digitalWrite(left_moto2,1);
   digitalWrite(left_moto4,0);
   analogWrite(pwmleft,100);
   analogWrite(pwmright,100);
 }
 void yuanyouBZ() //原地右转
 {
   digitalWrite(right_moto7,1);
   digitalWrite(right_moto8,0);
   digitalWrite(left_moto2,0);
   digitalWrite(left_moto4,1);
   analogWrite(pwmleft,100);
   analogWrite(pwmright,100);
 }
void ting()  // 停
{
    digitalWrite(right_moto7,0);
   digitalWrite(right_moto8,0);
   digitalWrite(left_moto2,0);
   digitalWrite(left_moto4,0);
   analogWrite(pwmleft,0);
   analogWrite(pwmright,0);
}
