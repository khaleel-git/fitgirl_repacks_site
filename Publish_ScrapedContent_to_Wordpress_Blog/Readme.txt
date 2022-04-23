How to Publish Scraped content to Wordpress Blog:
1-> First of all add these 2 functions to function.php (wordpress theme):

    function does_url_exists($url) # This function checks whether a blog post already posted or not?
    {
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_NOBODY, true);
        curl_exec($ch);
        $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        if ($code == 200) {
        $status = true;
        } else {
        $status = false;
        }
        curl_close($ch);
        return $status;
    } 
    
    # Below Function simply Upload image to Wordpress media library
    function upload_file($image_url, $post_id) 
    {
        $image = $image_url;
        // echo '$image is '; echo $image;echo'<br>';echo'<br>';

        $get = wp_remote_get($image);
        
        // echo '$get is '; echo $get;echo'<br>';echo'<br>';

        $type = wp_remote_retrieve_header($get, 'content-type');
        // echo '$type is ';echo $type;echo'<br>';echo'<br>';
        // $type = 'image/png';
        $type = 'image/webp';
        
        if (!$type) {
            return false;
        }
        $baseimage = basename($image);
        // echo '$baseimage is ';echo $baseimage; echo '<br>';echo'<br>';
        // echo $appId_image;
        $baseimage = $post_id.'_icon.png';
        // echo 'base image: ';echo $baseimage;
        // echo 'new $baseimage is ';echo $baseimage; echo '<br>';echo'<br>';

        #$mirror = wp_upload_bits(basename($image), '', wp_remote_retrieve_body($get));
        $mirror = wp_upload_bits($baseimage, '', wp_remote_retrieve_body($get));
        // echo '$mirror is ';echo'<br>';echo'<br>';
        // print_r($mirror);echo '<br>';
        // echo $mirror["file"];
        $old_image = $mirror["file"];

        $attachment = array(
            'post_title' => $baseimage,
            'post_mime_type' => $type
        );

        // echo '$attachement array is ';//echo $arrachment;echo'<br>';echo'<br>';
        // print_r($attachment);echo '<br>';

        $attach_id = wp_insert_attachment($attachment, $mirror['file'], $post_id);
        // echo '$attach_id is ';//echo $attach_id;echo'<br>';echo'<br>';
        // print_r($attach_id);echo '<br>';

        //convert image to webp
                                                
        // echo '<br>old image url: '; echo $old_image;echo '<br>';
        $info = getimagesize($old_image);
        // print_r($info);echo '<br>';
                                            
        //$output = shell_exec("cwebp -q 80 $old_image -o $old_image");
        // echo 'new image resiezed successfully';
        // echo "<pre>$output</pre>";
    
        // echo '<br>new image url: '; echo $old_image;echo '<br>';
        $info = getimagesize($old_image);
        // print_r($info);echo '<br>';
        

        // require_once(ABSPATH . 'wp-admin/includes/image.php');

        $attach_data = wp_generate_attachment_metadata($attach_id, $mirror['file']);

        wp_update_attachment_metadata($attach_id, $attach_data);

        return $attach_id;
    }

2-> content Folder contains .json files (These files are the scraped content)
3-> in process_links.php set loop counter to 20 (at a time 20 posts will be published to wordpres blog, and whenever a post is pblished the associate .json file will be deleted)
4-> if you are on linux -> set crontab to execute process_links.php file at every 1 minute 
    In your linux terminal, "type: crontab -e"
    add below line to crontab file: 
        * * * * wget your-domain.com/path/process_links.php  
    save your crontab file
    Now you linux server will publish 20 blog posts after every minute

5-> note! set your json file content carefully and please update your code in publish.php file according to json keys, thanks! enjoy.