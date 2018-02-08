void bluetooth()
{   
    char val=Serial.read();  //读取串口值并赋值给 val
  
                       /*  右轮调速  */
    if('j'==val) RSpeed-=5,Serial.print(RSpeed);//调速-5并输出当前的速度
    if('z'==val) RSpeed+=5,Serial.print(RSpeed);//调速+5并输出当前的速度
    
                      /*    蓝牙主控    */

    if('w'==val)  //前进
    { 
      strat=2;
      qian();
    }
    if ('s'==val)  //后退
    {
      strat=2;
      hou();
    }
    if('i'==val)  //停止
    {
      strat=2;
      ting();
    }
    if('a'==val)//左转
    {
       strat=2;
      zuo();
    }
     if('d'==val)//右转
    {
       strat=2;
      you();
    }
     if('q'==val)//左原地转
    {
       strat=2;
      yuanzuo();
    }
    if('e'==val)//右原地转
    {
       strat=2;
      yuanyou();
    }
    if('m'==val)//开启避障
    {
      strat=1;
    }
}
