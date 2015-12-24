#include <EtherCard.h>

// ethernet interface mac address, must be unique on the LAN
static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x32 };

byte Ethernet::buffer[700];
static uint32_t timer;

const char website[] PROGMEM = "dns1234.com";
String mContTyp="1";

//Struct
struct stParam{
 String typ;
 String count;
 String msg;
};

//get_Struct
struct stParam get_Struct(String sRes4){
    struct stParam param;
      param.typ     = sRes4.substring(0,2);
      param.count   = sRes4.substring(2,4);
      param.msg     = sRes4.substring(4);
    return param; 
}
//
void send_matrix(String src){
   int iLen=src.length();
   char sTmp[4+1];
   String sBuff="";
   String sCRLF="\r\n";
   char ss[64 +1];
   int iCt=0;
   Serial.print("011");
   src.toCharArray(ss, src.length()+1);
  for(int i=0; i< strlen(ss); i++){
    sprintf(sTmp, "%02x", (char *)ss[i]);
    sBuff= String(sTmp);
    if(sBuff.length() >=4){
      sBuff=sBuff.substring(2,4);
      Serial.print(sBuff);
    }
    iCt++;
    if(iCt>=  6){
        delay(100);
        iCt=0;
    }
  }
  Serial.print(sCRLF);
}

// called when the client request is complete
static void my_callback (byte status, word off, word len) {
  Serial.println(">>>");
  delay(500);
  
  Ethernet::buffer[off+300] = 0;
  //Serial.print((const char*) Ethernet::buffer + off);
  String response =(const char*) Ethernet::buffer + off;
  //Serial.println("...");
//Serial.println("response="+response);
  int iSt=0;
  struct stParam param;
  iSt = response.indexOf("res=");
  if(iSt >= 0){
    iSt = iSt+ 4;
    String sDat = response.substring(iSt );
    if(sDat.length() > 8){
      param= get_Struct(sDat);
      mContTyp= param.typ;
      send_matrix(param.msg);
    }
  } //end _iSt
}

void setup () {
  Serial.begin( 9600);
//  pinMode(mLED_pin, OUTPUT);
  Serial.println(("#Start-[webClient]"));

  if (ether.begin(sizeof Ethernet::buffer, mymac) == 0) 
    Serial.println(F("Failed to access Ethernet controller"));
  if (!ether.dhcpSetup())
    Serial.println(F("DHCP failed"));

//  ether.printIp("IP:  ", ether.myip);
//  ether.printIp("GW:  ", ether.gwip);  
//  ether.printIp("DNS: ", ether.dnsip);  

  if (!ether.dnsLookup(website))
    Serial.println("DNS failed");
    
  //ether.printIp("SRV: ", ether.hisip);
  delay( 5000 );
}

void loop () {
  ether.packetLoop(ether.packetReceive());
  if (millis() > timer) {
    timer = millis()   +15 * 1000;
    Serial.println();
    Serial.print("<<< REQ ");
    char sTyp[2 +1];
    mContTyp.toCharArray(sTyp, mContTyp.length()+1);
    char buff[32]="";
    sprintf(buff, "?typ=%s&ct=1", sTyp);
    ether.browseUrl(PSTR("/test_matrix_1223a.php"), buff, website, my_callback);
  }
}


