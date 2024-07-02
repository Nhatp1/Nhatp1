error_reporting(0);
session_start();
date_default_timezone_set("Asia/Ho_Chi_Minh");
$Ngay=`date "+%d/%m/%Y"`;
$Blue="\033[0;34m";
$red="\033[1;31m";
$xanh="\033[1;32m";
$white= "\033[1;37m";
$den = "\033[1;90m";
$do = "\033[1;91m";
$luc = "\033[1;92m";
$vang = "\033[1;33m";
$xduong = "\033[1;94m";
$hong = "\033[1;95m";
$trang = "\033[1;97m";
$do="\033[1;91m";
$Blue="\033[0;34m";
@system('clear');
$banner="\r
 \033[0;34m__  __ _       
 \033[1;32m____ _____
 \033[1;33m|  \/  | |        |
 \033[1;31m_ \__  /
 \033[1;33m| |\/| | |   _____| 
 \033[1;32m |/ / 
 \033[1;91m| |  | | |__|_____|
 \033[0;34m|_| / /_ 
 \033[1;31m|_|  |_|_____| 
 \033[1;33m|____/____|
 \033[1;31m────────────────────────────────────────────────────────────
 \033[1;31m[\033[1;37m=✓=\033[1;31m] \033[1;37m=> \033[1;31mTOOL GOLIKE INSTAGRAM
\033[1;33m[\033[1;37m=✓=\033[1;31m] \033[1;37m=> \033[1;35mADMIN: \033[1;97mNT-DZ
\033[1;31m[\033[1;37m=✓=\033[1;31m] \033[1;37m=> \033[1;32mThông báo ✓: \033[1;37mSắp tới sẻ ra mắc các tool 
\033[1;31m[\033[1;37m=✓=\033[1;31m] \033[1;37m=> \033[1;34mGolike tiktok: \033[1;37mTự Động Chuyển Jod Cực Mược
\033[1;31m[\033[1;37m=✓=\033[1;33m]=> \033[1;37mTrao Đổi Sud: \033[1;37mTrao Đổi Sud tik tok tds pro5 tds Instagram 
\033[1;31m────────────────────────────────────────────────────────────\n";
#echo $luc."\nVui lòng nhập AIP Key: $vang";
#$key =trim(fgets(STDIN));
#if($key=="vinhdztds"){
#	echo $vang."API Key Chính Xác!!!!\n ";
#	}
#	else {
#		exit($do."Key Không Hợp Lệ Vui Lòng Liên Hệ Để Mua Key hoac lay key free!!!\n");}
//cofig
                              
 system('clear');
 echo $banner;

$thanhngang = "\033[1;31m────────────────────────────────────────────────────────────\n";
$van = $do."[".$trang ."=.=".$do."] ".$trang."=> ";


if (file_exists("Authorization.json")) {
    echo $van."\033[1;32mBạn có muốn dùng lại Authorization ? " . $trang . "(Enter để sử dụng lại, Y để thay ) \033[1;37m=> \033[1;33m";
    $trl = trim(fgets(STDIN)); 
    if ($trl == "Y" or $trl == "y") {
    	unlink("Authorization.json");
        echo $van . " Authorization : ";
        $authorization = trim(fgets(STDIN));
        file_put_contents("Authorization.json", $authorization);
    } else {
        $authorization = file_get_contents("Authorization.json");
    } 
} else {
    echo $van."\033[1;32mNhập Authorization: \033[1;33m";
    $authorization = trim(fgets(STDIN));
    file_put_contents("Authorization.json", $authorization);
}

$authorization = file_get_contents("Authorization.json");


$url = "https://sv5.golike.net/api/users/me";
$tsm = array(
    "Host:sv5.golike.net",
    "accept:application/json, text/plain, */*",
    "authorization:".$authorization,
    "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.130 Mobile Safari/537.36",
    "content-type:application/json;charset=utf-8",
    "origin:https://app.golike.net",
);
$home = post_type($url, $tsm);
if ($home["success"] == 200) {
    echo $van."\033[1;32mĐĂNG NHẬP THÀNH CÔNG \n";
    $username = $home["data"]["username"];
    $coin = $home["data"]["coin"];

    sleep(1);
} else {
    echo $van."\033[1;31mĐĂNG NHẬP THẤT BẠI \n";
    exit;
}



$gop_data = [];
system('clear');
echo $banner;
////echo $van."\033[1;32mTÀI KHOẢN : ".$trang.$username." \n";
////echo $van."\033[1;32mSỐ DƯ : ".$trang.$coin." \n";
///echo $thanhngang;

if (file_exists("cookie_ig.txt")) {
    echo $van."\033[1;32mBạn có muốn dùng lại Cookie IG Cũ ? " . $trang . "(Enter để sử dụng lại, Y để thay ): ".$vang;
    $chon = trim(fgets(STDIN));
    if ($chon == "Y" || $chon == "y") {
        unlink("cookie_ig.txt");
    } else {
    	$gop_data = json_decode(file_get_contents("cookie_ig.txt"), true);
    }
}

if (!file_exists("cookie_ig.txt")) {
while(true){
	$s= $s+1 ;
	echo $van."\033[1;32mNhập Cookie Instagram Thứ $s : ".$vang;
	$nhap = trim(fgets(STDIN));
	if ( $nhap == ""){
	 	break;
	}else{
### echo cookie 
		$ck = get_info_ig($nhap);
		$giainen = explode('|', $ck);
		if (!$giainen){
			echo $van."\033[1;31mCookie Không Hợp Lệ \n";
			continue ;
		}else{
			$id_instagram = $giainen[1];
			$r = get_id($authorization);
			$tk_so = array_search($id_instagram, $_SESSION['ig']);
			$id = $_SESSION['id'][$tk_so];
			if (!$id){
				echo $van." \033[1;31mTÀI KHOẢN CHƯA ĐƯỢC CẤU HÌNH VÀO GOLIKE \n";
				continue;
			}
			$tong = $ck.'|'.$id;
			array_push($gop_data, $tong);
			fwrite(fopen("cookie_ig.txt","w"),json_encode($gop_data));
		}
	}
}}



echo $van."\033[1;32mNhập Delay : ".$trang;
$delay = trim(fgets(STDIN));
echo $van."\033[1;32mBao Nhiêu Job Thì Đổi Acc : ".$trang;
$doi = trim(fgets(STDIN));
system('clear');
echo $banner;
echo $van."\033[1;32mTÀI KHOẢN : ".$trang.$username." \n";
echo $van."\033[1;32mSỐ DƯ : ".$trang.$coin." \n";
echo $thanhngang;


while (true){
	if ($gop_data == [] ){
		while(true){
			$s= $s+1 ;
			echo $van."\033[1;32mNhập Cookie Instagram Thứ $s : ".$vang;
			$nhap = trim(fgets(STDIN));
			if ( $nhap == ""){
	 			break;
			}else{
### echo cookie 
				$ck = get_info_ig($nhap);
				$giainen = explode('|', $ck);
				if (!$giainen){
					echo $van." \033[1;31mCookie Không Hợp Lệ \n";
					continue ;
				}else{
					$id_instagram = $giainen[1];
					$r = get_id($authorization);
					$tk_so = array_search($id_instagram, $_SESSION['ig']);
					$id = $_SESSION['id'][$tk_so];
					$tong = $ck.'|'.$id;
					array_push($gop_data, $tong);
				}
			}
		}
	}
	
	foreach ($gop_data as $haha) {
		if (!$haha){
			break;
		}
		$giainen = explode('|', $haha);
		$idig = $giainen[0];
		$id_instagram = $giainen[1];
		$cookie = $giainen[2];
		$csrftoken = $giainen[3];
		$id_gl = $giainen[4];
		echo $van."\033[1;32mĐANG CHẠY TÀI KHOẢN : ".$vang.$id_instagram.$do." | ".$trang.$idig." \n";
		echo $thanhngang;
		####tìm job
		while(true){
			$list = get_job($authorization,$id_gl);
			
			if ($list["status"] == 200 ){
				$id_nhan = $list["data"]["id"];
				$object_id = $list["data"]["object_id"];
				$type = $list["data"]["type"];
				if ( $type == "follow"){
					$fl = follow($object_id,$cookie,$csrftoken);
					if ($fl = "ok"){
						echo $van."\033[1;32mFOLLOW SUCCESS \r";
						sleep(1);
					}else if($fl == 'die'){
						echo $van."\033[1;31mTài Khoản Bị Block \n";
						$tk_so = array_search($haha, $gop_data);
						unset($data_ig[$tk_so]);
						break;
					}else{
						echo $van." \033[1;31mLỖI KHÔNG XÁC ĐỊNH \n";
						
						
					}
				}else if( $type == "like"){
					$id_like = $list["data"]["object_data"];
					$js = json_decode($id_like,true);
					$id_l = $js["id"];
					
					$like = like($id_l,$cookie,$csrftoken);
					
					if ($like == 'die'){
						echo $van." \033[1;31mTài Khoản Bị Block \n";
						$tk_so = array_search($haha, $gop_data);
						unset($data_ig[$tk_so]);
						break;
					}
					
				}else{
					echo $van." \033[1;31mKHÔNG THỂ LÀM NHIỆM VỤ $type \n";
					continue;
				}
				
				$nhan_coin = nhan_job($authorization,$id_gl,$id_nhan);
				if ($nhan_coin["status"]== 200 ){
					$type_2 = $nhan_coin["data"]["type"];
					$gio = date("H:i");
					$tt = $tt+1;
					echo "".$do." | ".$BBlue.$tt.$do." | ".$luc.$gio.$do." | ".$trang.$type_2.$do." | ".$vang.$object_id.$do." | ".$BBlue."SUCCESS ".$do."|\n";
					if ($tt % $doi == 0){
						break;
					}
					delay($delay) ;
				}else{
					$l = $nhan_coin["message"];
					echo $van." \033[1;31mNHẬN THẤT BẠI $l \n";
					delay(10) ;
					continue;
				}
				
			}else{
				echo $list["message"]."\n";
				delay(10) ;
				break ;
			}
			
		}
		
	}
	
	
}

function delay($delay) {
    for ($time = $delay; $time > -1; $time--) {
        echo "\r\033[1;93m   Vui Lòng Chờ\033[1;97m ~>       \033[1;92m L\033[1;97m |\033[1;93m $time\033[1;97m | ";
        usleep(150000);

        echo "\r\033[1;91m   Vui Lòng Chờ\033[0;33m   ~>     \033[0;37m LO\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;92m   Vui Lòng Chờ\033[0;33m     ~>   \033[0;37m LOA\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;94m   Vui Lòng Chờ\033[0;33m       ~> \033[0;37m LOAD\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   Vui Lòng Chờ\033[0;33m        ~>\033[0;37m LOADI\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   Vui Lòng Chờ\033[0;33m        ~>\033[0;37m LOADIN\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(150000);
        echo "\r\033[1;95m   Vui Lòng Chờ\033[0;33m        ~>\033[0;37m LOADING.\033[0;31m |\033[0;33m $time\033[0;31m | ";
        usleep(100000);
        echo "\r                                          \r";
    }}
function like($id,$cookie,$csrftoken){
	$url = "https://www.instagram.com/api/v1/web/likes/".$id."/like/";
	$header = array(
	"Host:www.instagram.com",
	 "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.57 Mobile Safari/537.36",
	 "viewport-width:360",
	 "content-type:application/x-www-form-urlencoded",
	"accept:*/*",
	"x-requested-with:XMLHttpRequest",
	"x-asbd-id:198387",
	"x-csrftoken:".$csrftoken,
	"sec-ch-prefers-color-scheme:light",
	"x-ig-app-id:1217981644879628",
	"x-asbd-id:198387",
	"cookie:".$cookie,
	
	);
	$text = post_type3($url, $header);

	if ( $text["status"] == "ok" ){
		echo " \033[1;32mLIKE SUCCESS \r";
		return "ok";
	}else if ( $text["spam"] ){
		return "die";
	}else{
		 print_r($text);
		return "ko";
		
	}
}

function follow($id,$cookie,$csrftoken){
	$url = "https://www.instagram.com/api/v1/friendships/create/".$id."/";
	$tsm = array (
	"Host:www.instagram.com",
	"user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
	"viewport-width:360",
	"content-type:application/x-www-form-urlencoded",
	"accept:*/*",
	"x-requested-with:XMLHttpRequest",
	"x-asbd-id:129477",
	"x-csrftoken:".$csrftoken,
	"sec-ch-prefers-color-scheme:light",
	"x-ig-app-id:1217981644879628",
	"origin:https://www.instagram.com",
	"cookie:".$cookie,
	);
	$data = "container_module=profile&nav_chain=PolarisProfileRoot%3AprofilePage%3A1%3Avia_cold_start&user_id=".$id;
	$text = post_type2($url, $tsm, $data);
	if ( $text["status"] == "ok" ){
		echo " \033[1;32mFOLLOW SUCCESS \r";
		return "ok";
	}else if ( $text["spam"] ){
		return "die";
	}else{
		 print_r($text);
		return "ko";
	}
}

function get_info_ig($cookie){
  if (!strpos($cookie, 'ds_user_id') || !strpos($cookie, 'csrftoken')){
      return "cookie_err";
  }
  $idig = trim(explode(';',explode('ds_user_id=', $cookie)[1])[0]);
  $csrftoken = trim(explode(';',explode('csrftoken=', $cookie)[1])[0]);

  $ch = curl_init();
  curl_setopt($ch, CURLOPT_URL, 'https://i.instagram.com/api/v1/users/'.$idig.'/info/');
  curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
  curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'GET');
  curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');
  $headers = array();
  $headers[] = 'Authority: i.instagram.com';
  $headers[] = 'Sec-Ch-Ua: \"Google Chrome\";v=\"93\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"93\"';
  $headers[] = 'Sec-Ch-Ua-Mobile: ?0';
  $headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36';
  $headers[] = 'Accept: */*';
  $headers[] = 'X-Asbd-Id: 198387';
  $headers[] = 'Sec-Ch-Ua-Platform: \"Windows\"';
  $headers[] = 'X-Ig-App-Id: 936619743392459';
  $headers[] = 'Origin: https://www.instagram.com';
  $headers[] = 'Sec-Fetch-Site: same-site';
  $headers[] = 'Sec-Fetch-Mode: cors';
  $headers[] = 'Sec-Fetch-Dest: empty';
  $headers[] = 'Referer: https://www.instagram.com/';
  $headers[] = 'Accept-Language: en-US,en;q=0.9';
  $headers[] = 'Cookie: '.$cookie;
  curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
  $result = curl_exec($ch);
  if (curl_errno($ch)) {
     echo 'unknown';
  }
  curl_close($ch);

  if (!strpos($result, '"status":"ok"')){
    return "cookie_err";
  }
  $data = json_decode($result, true)['user'];
  $idig = $data['pk'];
  $username = $data['username'];
  echo $GLOBALS['vang']."GET Thành Công INSTAGRAM : ".$GLOBALS['luc'].$data['full_name']." ".$GLOBALS['vang']."Username: ".$GLOBALS['luc'].$username."\n";
  return $idig.'|'.$username.'|'.$cookie.'|'.$csrftoken;
}


function nhan_job($authorization,$id,$id_job){
	$data = '{"instagram_users_advertising_id":'.$id_job.',"instagram_account_id":'.$id.',"async":true,"data":null}';
	$url = "https://dev.golike.net/api/advertising/publishers/instagram/complete-jobs";
	$head = array(
	"Host:dev.golike.net",
	"content-length:96",
	"accept:application/json, text/plain, */*",
	"t:VFZSWk5FOVVVWGROUkUxNVQwRTlQUT09",
	"authorization:".$authorization,
	"user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
	"content-type:application/json;charset=UTF-8",
	"origin:https://app.golike.net",
	);
	$tt = post_type2($url, $head, $data);
	
	return $tt;
}
function get_job($authorization,$id){
	$url = "https://dev.golike.net/api/advertising/publishers/instagram/jobs?instagram_account_id=".$id."&data=null";
	$head = array (
	"Host:dev.golike.net",
	"accept:application/json, text/plain, */*",
	"t:VFZSWk5FOVVVWGROUkVsM1RtYzlQUT09",
	"authorization:".$authorization,
	"user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
	"content-type:application/json;charset=utf-8",
	"origin:https://app.golike.net",
	);
	$tt = post_type($url, $head);
	return $tt;
}
function get_id($authorization){
	$_SESSION['id'] = [] ;
	$_SESSION['ig'] = [] ;
	$url = "https://sv5.golike.net/api/instagram-account";
	$header = array(
	"Host:sv5.golike.net",
	"accept:application/json, text/plain, */*",
	"t:VFZSWk5FOVVVWGROUkVsM1RtYzlQUT09",
	"authorization:".$authorization,
	"user-agent:Mozilla/5.0 (Linux; Android 8.1.0; CPH1912 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36",
	"content-type:application/json;charset=utf-8",
	"origin:https://app.golike.net",
	);
	$tt = post_type($url, $header);
	if ($tt["success"]== 200 ){
		$sl = count($tt["data"]);
		for ($so = 0; $so < $sl ; $so++) {
		$id = $tt["data"][$so]["id"];
		$instagram_username = $tt["data"][$so]["instagram_username"];
		
		
		array_push($_SESSION['ig'], $instagram_username);
		array_push($_SESSION['id'], $id);
		
		}
		
	}else{
		echo " \033[1;31mGET THÔNG TIN CẤU HÌNH THẤT BẠI \n";
	}
	
}
function post_type2($url, $tsm, $data){
$mr = curl_init();
curl_setopt_array($mr, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => $data,
  CURLOPT_HTTPHEADER => $tsm));
$mr2 = curl_exec($mr); curl_close($mr);
$js = json_decode($mr2,true);
return $js;
}
function post_type($url, $tsm){
$mr = curl_init();
curl_setopt_array($mr, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => $tsm));
$mr2 = curl_exec($mr); curl_close($mr);
$js = json_decode($mr2,true);
return $js;
}

function post_type3($url, $tsm){
	##$ip = explode(':',$ipp);
$mr = curl_init();
curl_setopt_array($mr, array(
  CURLOPT_PORT => "443",
  CURLOPT_URL => "$url",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_SSL_VERIFYPEER => false,
  CURLOPT_TIMEOUT => 30,
  ##CURLOPT_PROXY => $ip[0],
  ##CURLOPT_PROXYPORT => $ip[1],
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_HTTPHEADER => $tsm));
$mr2 = curl_exec($mr); curl_close($mr);
$js = json_decode($mr2,true);
return $js;
}
