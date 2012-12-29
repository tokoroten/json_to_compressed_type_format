>>print "--object number"
--object number

>print json_to_compressed_type_format("1")
int

>print json_to_compressed_type_format("1.1")
float

>print json_to_compressed_type_format("100000000000")
long

>print "--object str"
--object str

>print json_to_compressed_type_format('"hoge"')
str

>print "--object list"
--object list

>print json_to_compressed_type_format('["hoge", 1, 1.1]')
[int, float, str]

>print "--object dict normal"
--object dict normal

>print json_to_compressed_type_format('{"age":9, "gender":"Female", "name":"sakura"}')
{name:str, age:int, gender:str}


>print "--object dict simple"
--object dict simple

>print json_to_compressed_type_format('{"age":9, "gender":"Female", "name":"sakura"}', True)
{str:int, str:str}

>print "--nested object"
--nested object

>print json_to_compressed_type_format('''[
        {"age":9, "gender":"Female", "name":"sakura"},
        {"age":10, "gender":"Male", "name":"xaolong"}
]''')
[{name:str, age:int, gender:str}]

>print "--twitter json sample"
--twitter json sample

>twitter_json = open("./sample.json").read()

>print "--normal mode--"
--normal mode--

>print json_to_compressed_type_format(twitter_json)
[{truncated:bool, retweeted:bool, place:null, in_reply_to_user_id:null, id_str:str, in_reply_to_status_id_str:null, user:{time_zone:str, lang:str, show_all_inline_media:bool, following:null, profile_sidebar_border_color:str, description:str, verified:bool, protected:bool, profile_sidebar_fill_color:str, default_profile_image:bool, notifications:null, friends_count:int, id:int, profile_background_color:str, id_str:str, followers_count:int, created_at:str, listed_count:int, geo_enabled:bool, statuses_count:int, utc_offset:int, profile_background_image_url_https:str, profile_background_tile:bool, profile_use_background_image:bool, name:str, profile_text_color:str, is_translator:bool, default_profile:bool, contributors_enabled:bool, favourites_count:int, url:str, profile_background_image_url:str, location:str, follow_request_sent:null, screen_name:str, profile_image_url_https:str, profile_link_color:str, profile_image_url:str}, text:str, id:long, coordinates:null, retweet_count:int, source:str, in_reply_to_screen_name:null, geo:null, possibly_sensitive:bool, contributors:null, in_reply_to_status_id:null, created_at:str, favorited:bool, in_reply_to_user_id_str:null}, {truncated:bool, retweeted:bool, place:null, in_reply_to_user_id:null, id_str:str, in_reply_to_status_id_str:null, user:{time_zone:str, lang:str, show_all_inline_media:bool, following:null, profile_sidebar_border_color:str, description:str, verified:bool, protected:bool, profile_sidebar_fill_color:str, default_profile_image:bool, notifications:null, friends_count:int, id:int, profile_background_color:str, id_str:str, followers_count:int, created_at:str, listed_count:int, geo_enabled:bool, statuses_count:int, utc_offset:int, profile_background_image_url_https:str, profile_background_tile:bool, profile_use_background_image:bool, name:str, profile_text_color:str, is_translator:bool, default_profile:bool, contributors_enabled:bool, favourites_count:int, url:str, profile_background_image_url:str, location:str, follow_request_sent:null, screen_name:str, profile_image_url_https:str, profile_link_color:str, profile_image_url:str}, text:str, id:long, coordinates:null, retweet_count:int, source:str, in_reply_to_screen_name:null, geo:null, contributors:null, in_reply_to_status_id:null, created_at:str, favorited:bool, in_reply_to_user_id_str:null}]

>print "--simple mode--"
--simple mode--

>print json_to_compressed_type_format(twitter_json, True)
[{str:bool, str:str, str:null, str:long, str:{str:null, str:bool, str:int, str:str}, str:int}]