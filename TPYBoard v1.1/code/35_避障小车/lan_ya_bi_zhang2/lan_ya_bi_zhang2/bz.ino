void bz()
{
        BZQL=digitalRead(13);BZQR=digitalRead(12);//读取前面的避障模块状态
        BZL=digitalRead(11);BZR=digitalRead(10);//读取侧面的避障模块状态
        
/*******************************  前 进  *************************************/
        if(BZQL==HIGH&&BZQR==HIGH&&BZL==HIGH&&BZR==HIGH)
        {
          qianBZ();
        }
        if(BZQL==HIGH&&BZQR==HIGH&&BZL==LOW&&BZR==LOW)
        {
          qianBZ();
        }
        
/*****************************  一个避障传感器的状态  ************************/
        if(BZQL==LOW&&BZQR==HIGH&&BZL==HIGH&&BZR==HIGH)
        {
          yuanyouBZ();
          pd=0;
        }
        if(BZQL==HIGH&&BZQR==LOW&&BZL==HIGH&&BZR==HIGH)
        {
          yuanzuoBZ();
          pd=1;
        }        
        if(BZQL==HIGH&&BZQR==HIGH&&BZL==LOW&&BZR==HIGH)
        {
          yuanyouBZ();
          pd=0;
        }        
        if(BZQL==HIGH&&BZQR==HIGH&&BZL==HIGH&&BZR==LOW)
        {
          yuanzuoBZ();
          pd=1;
        }
/***************************  两个避障传感器的状态  *************************/  
        
       /*********************  左转  **********************/
         if(BZQL==HIGH&&BZQR==LOW&&BZL==HIGH&&BZR==LOW)
        {
          yuanzuoBZ();
          pd=1;
        }
        if(BZQL==LOW&&BZQR==HIGH&&BZL==HIGH&&BZR==LOW)
        {
          hou();
          delay(100);
          yuanzuoBZ();
          pd=1;
        }
        if(BZQL==LOW&&BZQR==LOW&&BZL==HIGH&&BZR==HIGH&&pd==1)
        {
          yuanzuoBZ();
        }
        
      /*********************  右转  ***************************/
          if(BZQL==LOW&&BZQR==HIGH&&BZL==LOW&&BZR==HIGH)
        {
          yuanyouBZ();
          pd=0;
        }
        if(BZQL==HIGH&&BZQR==LOW&&BZL==LOW&&BZR==HIGH)
        {
          pd=0;
          hou();
          delay(100);
          you();
        }
        if(BZQL==LOW&&BZQR==LOW&&BZL==HIGH&&BZR==HIGH&&pd==0)
        {
          yuanyouBZ();
        }
    
/***************************  三个避障传感器的状态  *************************/  
        if(BZQL==LOW&&BZQR==LOW&&BZL==LOW&&BZR==HIGH)
        {
          hou();
          delay(100);
          you();
        }
        if(BZQL==HIGH&&BZQR==LOW&&BZL==LOW&&BZR==LOW)
        {
          hou();
          delay(100);
          zuo();
        }
        if(BZQL==LOW&&BZQR==HIGH&&BZL==LOW&&BZR==LOW)
        {
          hou();
          delay(100);
          you();
        }
        if(BZQL==LOW&&BZQR==LOW&&BZL==HIGH&&BZR==LOW)
        {
          hou();
          delay(100);
          zuo();
        }
/***************************  四个避障传感器的状态  *************************/  
        if(BZQL==LOW&&BZQR==LOW&&BZL==LOW&&BZR==LOW)
        {
          hou();
        }
}
