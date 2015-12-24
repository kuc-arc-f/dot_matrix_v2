<?php
// マルチバイト対応
date_default_timezone_set('Asia/Tokyo');

class AppConst {
	var $mMSG_Const="メリークリスマス";
	var $mTYP_Kotei= 1;
	var $mTYP_Time = 2;
	var $mTYP_Date = 3;
	var $mTYP_Wdat = 4;

	var $mWCT_Area =1;
	var $mWCT_Cond =2;
	var $mWCT_Htmp =3;
	var $mWCT_Ltmp =4;
}
	
//------------------------------------
// @calling
// @purpose : Zero Str, max=10 char
// @date
// @argment
// @return
//------------------------------------
function getZeroStr( $src, $num ){
	if($num > 10){
		return "";
	}
	$buff="0000000000";

	$buff = $buff . $src;
	$i_len = strlen($buff);
	$ret = substr($buff, $i_len - $num, $num);
	
	return $ret;
}

//
function get_nextBody($aTyp, $aCt){
	$clsConst = new AppConst();
	$ret="";
	$iCt=0;
	$buffTyp="";
	$buffCt="";
	if ( $aTyp < $clsConst->mTYP_Date){
		$iCt = $aTyp + 1;
		$buffTyp=getZeroStr($iCt, 2);
		$buffCt =getZeroStr("00", 2);
		switch ($aTyp) {
			case 1:
				$ret=$buffTyp . $buffCt . $clsConst->mMSG_Const;
				break;
			case 2:
				$sHH = date("H");
				$sMM = date("i");
			    $sHH = mb_convert_kana($sHH, 'KVRN', "UTF-8");
			    $sMM = mb_convert_kana($sMM, 'KVRN', "UTF-8");
				$ret=$buffTyp . $buffCt . "じかん　" . $sHH . "：" . $sMM;
				break;
		}
	}else{
			$sMM = date("m");
			$sDD = date("d");
			$sMM = mb_convert_kana($sMM, 'KVRN', "UTF-8");
			$sDD = mb_convert_kana($sDD, 'KVRN', "UTF-8");
			$buffTyp = getZeroStr( $clsConst->mTYP_Kotei, 2);
			$buffCt =getZeroStr("00", 2);
			$ret=$buffTyp . $buffCt . "ひづけ　" . $sMM . "ー" . $sDD;
	}
	return $ret;
}


//------------------------------------
// @calling : main
// @purpose : 
// @date
// @argment
// @return
//------------------------------------
	$ret_base= "000000000000000000000000";
	$sHEAD ="res=";
	$respose="";
    $res2="あいうテスト";
    if(isset($_GET["typ"])){
	    if(isset($_GET["ct"])){
	    	$aTyp= $_GET["typ"];
	    	$aCt= $_GET["ct"];
	    	$res2 = get_nextBody($aTyp, $aCt);
			echo $sHEAD .$res2;
	    }
    }else{
		echo $sHEAD .$ret_base;
    }
?>