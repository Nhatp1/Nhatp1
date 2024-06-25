


date_default_timezone_set('Asia/Ho_Chi_Minh');
header("Content-type: application/json");


$id          = round(microtime(true) * 1000);


 $username    = $_GET['account'];

    $password     = $_GET['password'];
$name_file = "cookie/".$username.".mp3";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, "https://gas.nvn.id.vn/api/prelogin.php?account=$username&format=json&id=$id&app_id=10000o");
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    curl_setopt($ch, CURLOPT_ENCODING, TRUE);
        $prelogin = curl_exec($ch);
            curl_close($ch);
           
        $preloginData = json_decode($prelogin, true);
       
                $passone = $preloginData['v1'];
            $passtwo = $preloginData['v2'];
             $idn = $id;

             if ($preloginData['account'])
             {




     $encryptedpw = EnCode(md5($_GET['password']),hash('sha256',hash('sha256',md5($_GET['password']).$preloginData['v1']).$preloginData['v2']));
    $ch = curl_init(); 

curl_setopt($ch, CURLOPT_URL, "https://connect.garena.com/api/login?account=$username&password=$encryptedpw&format=json&id=$id&app_id=10100");
curl_setopt($ch, CURLOPT_COOKIEJAR, dirname(__FILE__) . "/cookie/" . $username . ".mp3");
curl_setopt($ch, CURLOPT_COOKIEFILE, dirname(__FILE__) . "/cookie/" . $username . ".mp3");
curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt($ch, CURLOPT_ENCODING, true);
$prelogin = curl_exec($ch);
curl_close($ch);
//die($prelogin);
    $checkk = json_decode($prelogin);
    if ($checkk->username == $username) {
  $head = array(
                "Host: account.garena.com",
                "Connection: keep-alive",
                "sec-ch-ua-mobile: ?1",
                "User-Agent: Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36",
                "Accept: */*",
                "Sec-Fetch-Site: same-origin",
                "Sec-Fetch-Mode: cors",
                "Sec-Fetch-Dest: empty",
                "Accept-Language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5"
            );
            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, "https://account.garena.com/api/account/init");
            curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
            curl_setopt($ch, CURLOPT_COOKIEFILE, dirname(__FILE__) . "/cookie/" . $username . ".mp3");
            curl_setopt($ch, CURLOPT_COOKIEJAR, dirname(__FILE__) . "/cookie/" . $username . ".mp3");
            curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
            curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
            curl_setopt($ch, CURLOPT_ENCODING, true);
            $data3 = json_decode(curl_exec($ch), true);
            curl_close($ch);
            $shell = $data3["user_info"]["shell"];
            $nickname = $data3["user_info"]["nickname"];
            $uid = $data3["user_info"]["uid"];
            $level = $data3["user_info"]["level"];
            $mobile_no = $data3["user_info"]["mobile_no"];
            $suspicious = $data3["user_info"]["suspicious"];
            $email_v = $data3["user_info"]["email_v"];
            $fb_account = $data3["user_info"]["fb_account"];
            $authenticator_enable = $data3["user_info"]["authenticator_enable"];
            $idfb = $data3["user_info"]["fb_account"]["fb_uid"];
            $idc = $data3["user_info"]["idcard"];
            if ($idfb !== null) {

                $ch = curl_init();
                curl_setopt($ch, CURLOPT_URL, "https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id=$idfb");
                curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
                curl_setopt($ch, CURLOPT_ENCODING, true);
                $data = curl_exec($ch);
                curl_close($ch);
                //echo $data;
                if ($data == "live") {
                    $link = "Live";
                } else if ($data == "die") {
                    $link = "Die";
                } else {
                    $link = "No";
                }

            } else {

                $link = "No";

            }

            if ($idc !== null) {
                $cmnd = "Đã Xác Thực";

            } else {
                $cmnd = "Không";
            }
            $_SESSION['cmnd'] = $cmnd;








            $ch = curl_init();
            curl_setopt($ch, CURLOPT_URL, 'https://connect.garena.com/ui/login?app_id=10043&redirect_uri=https%3A%2F%2Fpvp.garena.vn%2F%3Flocale_name%3DVN&locale=vi-VN');
            curl_setopt($ch, CURLOPT_COOKIEJAR, dirname(__FILE__) . "/cookie/" . $username . ".mp3");
            curl_setopt($ch, CURLOPT_COOKIEFILE, dirname(__FILE__) . "/cookie/" . $username . ".mp3");
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
            curl_setopt($ch, CURLOPT_TIMEOUT, 60);
            curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 60);
            curl_setopt($ch, CURLOPT_FOLLOWLOCATION, TRUE);
            curl_setopt($ch, CURLOPT_HTTPHEADER, array('Expect:'));
            curl_setopt($ch, CURLOPT_HEADER, 1);
            $data_account = curl_exec($ch);

            curl_close($ch);
            $session = explode("\n", explode('session_key=', $data_account)[1])[0];
            curl_close($ch);
          
            $name_file = "cookie/".$username.".mp3";
            $datatest =  curl("https://auth.garena.com/oauth/token/grant", 'client_id=100054&response_type=token&redirect_uri=https%3A%2F%2Fkientuong.lienquan.garena.vn%2Fauth%2Flogin%2Fcallback&format=json&id='.$id.'', '', true, true, $name_file);
            //die(json_encode($datatest));
                    $linkkk = get_string_between($datatest[1],'"redirect_uri": "','"');
             $nvntoken = get_string_between($datatest[1],'"access_token": "','"');
            //die($nvntoken);
                  //  $datatest1 =  curl($linkkk, false, '', true, true, $name_file);
            //$nvntoken = 'de0495aaad03dc3d84c34fd9208d2d3991f3c0a5416e0470554290771f093331';
            $datatest1 = curl("https://kientuong.lienquan.garena.vn/auth/login/callback?access_token=$nvntoken", false, '', true, true, $name_file);
            
            
            //die(json_encode($datatest1));
                    $datatest2 =  curl('https://kientuong.lienquan.garena.vn/api/player/get', false, '', true, true, $name_file);
            
            //die($datatest2[1]);
            $nvndata = json_decode($datatest2[1], true);
            $name = $nvndata['player']['name'];
            $level = $nvndata['player']['level'];
            $regtime = $nvndata['player']['registerTime'];
            
            
             $ch=curl_init();
                curl_setopt($ch, CURLOPT_URL, 'https://sale.lienquan.garena.vn/login/callback?access_token='.$nvntoken);
                curl_setopt($ch, CURLOPT_COOKIEJAR, dirname(__FILE__) . "/cookie/" . $username . ".txt");
                curl_setopt($ch, CURLOPT_COOKIEFILE, dirname(__FILE__) . "/cookie/" . $username . ".txt");
                curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
                curl_setopt($ch, CURLOPT_ENCODING, true);
                $c = curl_exec($ch);
                curl_close($ch);
                    
                    
                $head = array(
                    'Host: sale.lienquan.garena.vn',
                    'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="98"',
                    'accept: */*',
                    'content-type: application/json',
                    'sec-ch-ua-mobile: ?1',
                    'user-agent: Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.89 Mobile Safari/537.36',
                    'sec-ch-ua-platform: "Android"',
                    'origin: https://sale.lienquan.garena.vn',
                    'sec-fetch-site: same-origin',
                    'sec-fetch-mode: cors',
                    'sec-fetch-dest: empty',
                    'referer: https://sale.lienquan.garena.vn/',
                    'accept-language: vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5'
                    );
                    $ch=curl_init();
                curl_setopt($ch, CURLOPT_URL, 'https://sale.lienquan.garena.vn/graphql');
                curl_setopt($ch, CURLOPT_COOKIEJAR, dirname(__FILE__) . "/cookie/" . $username . ".txt");
                curl_setopt($ch, CURLOPT_COOKIEFILE, dirname(__FILE__) . "/cookie/" . $username . ".txt");
                curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
                curl_setopt($ch, CURLOPT_HTTPHEADER, $head);
                curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
                curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
                curl_setopt($ch, CURLOPT_ENCODING, true);
                curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
                curl_setopt($ch, CURLOPT_POSTFIELDS, '{"operationName":"getUser","variables":{},"query":"query getUser {\n  getUser {\n    id\n    name\n    icon\n    profile {\n      ownedItemIdList\n      __typename\n    }\n    __typename\n  }\n}\n"}');
                $info_trangphuc = json_decode(curl_exec($ch));
                curl_close($ch);
                $sotuong = count($info_trangphuc->data->getUser->profile->ownedItemIdList); 
            
             $url = "https://weeklyreport.moba.garena.vn/api/profile";
            
            $headers = [
                "accept: application/json, text/plain, */*",
                "accept-language: vi,vi-VN;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5",
                "access-token: $nvntoken",
                "partition: 1011",
                "priority: u=1, i",
                "referer: https://weeklyreport.moba.garena.vn/portrait/recall",
                "sec-fetch-dest: empty",
                "sec-fetch-mode: cors",
                "sec-fetch-site: same-origin",
                "user-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
            ];
            
            $ch = curl_init();
            
            curl_setopt($ch, CURLOPT_URL, $url);
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
            curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
            
            $nvnrq = curl_exec($ch);
            $data = json_decode($nvnrq, true);
            //die($data);
            $player_rank = $data['player_info']['rank'];
            
            // Find the corresponding rank name
            $rank_config = $data['rank_config'];
            $rank_name = '';
            
            foreach ($rank_config as $rank_id => $rank_info) {
                if ($rank_id == $player_rank) {
                    $rank_name = $rank_info['name'];
                    break;
                }
            }
            curl_close($ch);
            // Output the rank name
            $RankReal = $rank_name;

            $QuanHuy = '';
            $rq4 = CurlNVN("https://auth.garena.com/oauth/token/grant", 'client_id=10017&redirect_uri=https%3A%2F%2Fnapthe.vn%2Fapp&response_type=token&platform=1&locale=vi-VN&theme=mshop_iframe_white&format=json&id=1654048860433&app_id=10017', '', dirname(_FILE_) . "/cookie/$username.mp3", dirname(_FILE_) . "/cookie/$username.mp3");
            $Data3 = json_decode($rq4);
            $token = Get_String($rq4[0], '{"access_token": "', '", ');
            $tokennlogin = '{"token":"' . $token . '"}';
            $check = CurlNVN("https://napthe.vn/api/auth/inspect_token", $tokennlogin, '', dirname(_FILE_) . "/cookie/$username.mp3", dirname(_FILE_) . "/cookie/$username.mp3");
            $StringGetCookie = Get_String($check[0], 'Set-Cookie:', ';');
            $headers = array(
                'Cookie: ' . $StringGetCookie . ''
            );
            $Start_ts = strtotime("-60 days");
            $End_ts = strtotime("now");
            $c = curl_init();
            curl_setopt($c, CURLOPT_URL, "https://napthe.vn/api/shop/history?app_id=100054&start_ts=$Start_ts&end_ts=$End_ts&region=VN&language=vi&limit=20&offset=0");
            curl_setopt($c, CURLOPT_SSL_VERIFYPEER, false);
            curl_setopt($c, CURLOPT_SSL_VERIFYHOST, false);
            curl_setopt($c, CURLOPT_FOLLOWLOCATION, true);
            curl_setopt($c, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($c, CURLOPT_HTTPHEADER, $headers);
            $rqe = curl_exec($c);
            curl_close($c);
            $a = 0;
            $b = 0;
            $json = json_decode($rqe, true);
            while ($json["items"][$a++]["point_amount"]) {
                $sum += $json["items"][$b++]["point_amount"];
            }
            $QuanHuy = $sum;
            if ($QuanHuy == "") {
                $QuanHuy = "Unknown";
            }


            
          //  $level = explode('"', explode('pvp_level":"', $data_accounts)[1])[0];
            $_SESSION['sotuong'] = $sotuong;
            $_SESSION['level'] = $level;
            $_SESSION['fb'] = $link;
            $_SESSION['cmnd'] = $cmnd;
            $_SESSION['QuanHuy'] = $QuanHuy;
            $_SESSION['email_active'] = $em;
            if ($email_v !== 0) {
                $email_v = "Email: Yes";
                $email_v_z = "yes";
                $_SESSION['nvnemail'] = $email_v_z;
            } else {
                $email_v = "Email: No";
                $email_v_z = "no";
                $_SESSION['nvnemail'] = $email_v_z;
            }
            if (strpos($mobile_no, '*') !== false) {
                $mobile_no = "Sdt: Yes";
                $mobile_no_z = "yes";
            } else {
                $mobile_no = "Sdt: No";
                $mobile_no_z = "no";
            }
            if ($fb_account !== null) {
                $fb_account = "LK FB: Yes";
            } else {
                $fb_account = "LK FB: No";
            }
            if ($email_v_z == 'no' && $mobile_no_z == 'no' && $suspicious == false) {
                $loaiacc = "Trắng Thông Tin";


            } else if ($email_v_z == 'no' && $mobile_no_z == 'no' && $suspicious == true) {
                $loaiacc = "Trắng Thông Tin Lỗi Pass";
            } else {

                $loaiacc = "Dính Thông Tin";

            }
   
 $nvn = $username . '|' . $password . '| Trạng Thái : ' . $loaiacc . '| Level : ' . $level . ' | Rank : ' . $RankReal . ' | Trang Phục : ' . $sotuong . '| Ngày Tạo : ' . date('H:i:s d-m-Y', $regtime) . '| QH đã nạp : ' . $QuanHuy . '| CMND : ' . $cmnd . ' | ' . $email_v . ' | ' . $mobile_no . '| FB : ' . $link . PHP_EOL;


    } else {

        $print = array(
            'result' => array(
                'status' => 'error',
                'Author' => 'Nong Van Nguyen'
            ),
            'username' => $username,
            'msg' => 'Mat khau sai'
        );
    $nvn = json_encode($print, JSON_PRETTY_PRINT);
    }
    
             } else {

                $print = array(
                    'result' => array(
                        'status' => 'error',
                        'Author' => 'Nong Van Nguyen'
                    ),
                    'username' => $username,
                    'msg' => 'Tai khoan khong ton tai'
                );
            $nvn = json_encode($print, JSON_PRETTY_PRINT);



             }

             echo $nvn;


    function EnCode($plaintext,$key)
    {
          $chiperRaw = openssl_encrypt(hex2bin($plaintext), "AES-256-ECB", hex2bin($key), OPENSSL_RAW_DATA);
          return substr(bin2hex($chiperRaw),0,32);
    }
   function CurlNVN($url, $post = false, $ref = '', $cookie = false, $cookies = false, $header = true, $headers = false, $follow = false)
{
    $ch = curl_init($url);
    if ($ref != '') {
        curl_setopt($ch, CURLOPT_REFERER, $ref);
    }
    if ($cookie) {
        curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    }
    if ($cookies) {
        curl_setopt($ch, CURLOPT_COOKIEJAR, $cookies);
        curl_setopt($ch, CURLOPT_COOKIEFILE, $cookies);
    }
    if ($post) {
        curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
        curl_setopt($ch, CURLOPT_POST, 1);
    }
    if ($follow)
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    if ($header)
        curl_setopt($ch, CURLOPT_HEADER, 1);
    if ($headers)
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_ENCODING, '');
    //curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($ch, CURLOPT_TIMEOUT, 15);

    //curl_setopt($ch, CURLINFO_HEADER_OUT, true);
    $result[0] = curl_exec($ch);
    $header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    $result[1] = substr($result[0], $header_size);
    curl_close($ch);
    return $result;

}

function Get_String($string, $start, $end)
{
    $string = ' ' . $string;
    $ini = strpos($string, $start);
    if ($ini == 0)
        return '';
    $ini += strlen($start);
    $len = strpos($string, $end, $ini) - $ini;
    return substr($string, $ini, $len);
}

function curl($url,$post = false,$ref = '', $cookie = false,$cookies = false, $name_file, $header = true,$headers = false,$follow = false)
{
    $ch=curl_init($url);
    if($ref != '') {
        curl_setopt($ch, CURLOPT_REFERER, $ref);
    }
    if($cookie){
    curl_setopt($ch, CURLOPT_COOKIE, $cookie);
    }
    if($cookies)
    {
    curl_setopt($ch, CURLOPT_COOKIEJAR, $name_file);
    curl_setopt($ch, CURLOPT_COOKIEFILE, $name_file);
    }
    if($post){
    curl_setopt($ch, CURLOPT_POSTFIELDS, $post);
    curl_setopt($ch, CURLOPT_POST, 1);
    }
    if($follow) curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    if($header)     curl_setopt($ch, CURLOPT_HEADER, 1);
    if($headers)        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    curl_setopt($ch, CURLOPT_ENCODING, '');
    //curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
      curl_setopt($ch, CURLOPT_TIMEOUT, 15);

        //curl_setopt($ch, CURLINFO_HEADER_OUT, true);
    $result[0] = curl_exec($ch);
    $header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    $result[1] = substr($result[0], $header_size);
    curl_close($ch);
    return $result;

}
function get_string_between($string, $start, $end){
    $string = ' ' . $string;
    $ini = strpos($string, $start);
    if ($ini == 0) return '';
    $ini += strlen($start);
    $len = strpos($string, $end, $ini) - $ini;
    return substr($string, $ini, $len);
}
    ?>
