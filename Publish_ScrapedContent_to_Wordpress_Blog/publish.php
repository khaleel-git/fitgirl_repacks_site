<?php     
  

											$modified_body = str_replace("&lt;", "<", $json_obj['body']);
											$modified_body = str_replace("&gt;", ">", $modified_body);

											$post_title = $json_obj['title'];
											// echo "<br><br>############################################<br>Post Title: $post_title <br>";
											// echo "Full Description: "; echo $json_obj['descriptionHtml'];echo "<br>";
											$post_title = str_replace("&", "&amp;", $post_title);
											$post_title = str_replace("–", "-", $post_title);
                                        	
											// if(isset($json_obj['details']['appDetails']['appType'])){
											// echo "apptype -> category: ";echo $json_obj['details']['appDetails']['appType'];echo "<br>";
                                            $category_name_01 = 'FitGirl-Repack';
											$category_name_02 = 'Desktop Games';
                                            		// echo $category_name;
                                            // }
											// else {$category_name = "apps";}
											$category_01 = get_category_by_slug( $category_name_01 );
											$category_02 = get_category_by_slug( $category_name_02 );

											// global $wpdb; $count = $wpdb->get_var("select COUNT(*) from $wpdb->posts where post_title like '$post_title' ");
											$count = 1;
											$string = str_replace(' ', '-', $json_obj['title']); // Replaces all spaces with hyphens.
   											$string = preg_replace('/[^A-Za-z0-9\-]/', '', $string); // Removes special chars.
   											$title_with_dashes = preg_replace('/-+/', '-', $string); // Replaces multiple hyphens with single one.
                    
											$title_with_dashes = strtolower($title_with_dashes);											                                      
                                        	$permalink_var = ''.$title_with_dashes.'/';
											echo "Permalink is: $permalink_var <br>";
											$file_pointer = "https://apkfuel.com/journal/$permalink_var";
// 											echo "<br>Post link is: $file_pointer <br>";
											
											 if (!does_url_exists($file_pointer)) {
            										echo "Post does not exist, Publishing the post now ... <br>";
                                             		$count = 0;                                            		
        										}
										
										if ($count == 0)
										{
                                        	
											$my_post = array(
  											'post_title'    => $post_title ,
  											'post_content'  => $modified_body,
  											'post_status'   => 'publish',
  											'post_author'   => 1,
  											'post_category' => array( $category_01->term_id , $category_02->term_id) 
											);

											$post_id = wp_insert_post( $my_post );
											// $url = $json_obj['icon'];
                                        	$url = $json_obj['first_img'];
                                        	$second_url = $json_obj['second_img'];
                                        
                                        	if (!does_url_exists($url)) {
                                            		echo "First image does not exist ...". $url . " <br>"; 
                                            
                                            		if (!does_url_exists($second_url)) {
                                                    
                                                    	echo "Second image does not exist ." . $second_url ." <br>";                                                     	
                                            			$ran = array(3932,3933,3934,3935,3936, 3937);
                                                    	$thumbnail_id = $ran[array_rand($ran, 1)];
                                            			echo "Thumbnail id is: ";
                                            			echo $thumbnail_id;
                                            			echo "<br>";
                                                    }
                                                    else {
                                                    	
                                                    	$r = upload_file($second_url, $appId);
														$thumbnail_id = $r;
                                                    }
            																						
        										}
                                        	else {
                                          
												$r = upload_file($url, $appId);
												$thumbnail_id = $r;
                                            }
                                        	
											set_post_thumbnail( $post_id, $thumbnail_id );										
											
                                       
                                        	$string = str_replace(' ', '-', $json_obj['title']); // Replaces all spaces with hyphens.
   											$string = preg_replace('/[^A-Za-z0-9\-]/', '', $string); // Removes special chars.
   											$title_with_dashes = preg_replace('/-+/', '-', $string); // Replaces multiple hyphens with single one.
                    
											$title_with_dashes = strtolower($title_with_dashes);
											// add_post_meta($post_id, 'custom_permalink', ''.$title_with_dashes.'/'.$appId.'/', true);
                                        
                                        	$permalink_var = ''.$title_with_dashes.'/';                                        
											
                                        	add_post_meta($post_id, 'rank_math_title', $post_title." - fitgirl (100% Working)",true);
                                            add_post_meta($post_id, 'rank_math_description',$json_obj['title'] . 'Free Download Fitgirl Repacks Games - latest [updated] 100% Working Download Links ...' ,true);
                                        	//set apk rating
                                   	
                                        	$date = date("Y-m-d");
                                    	
                                        	
                                        	echo "Success! Post Published. Post link is: $file_pointer <br>";
                                        	
                                        	$path    = "/home/apkfuel/public_html/journal/bulk_publish_posts/content/$appId.json";
                                        	unlink($path);
                                        	
                                       		// end of if statement
                                        }
										else 
                                        {
                                        	echo "Post already exists on apkfuel.com. Post link: $file_pointer <br>";
                                        	$path    = "/home/apkfuel/public_html/journal/bulk_publish_posts/content/$appId.json";
                                        	unlink($path);
                                        	
                                                                            
                                        }
										
                                        
                                        
											
?>