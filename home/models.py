from django.db import models
from django.contrib.auth.models import User


# Create your banner modee


class Logo(models.Model):
    logo_img = models.ImageField(upload_to='media')
    logo_alt =  models.CharField(max_length=20)


class Banner(models.Model):
    """
    model class for storing banner image

    """
    banner_img = models.ImageField(upload_to='media')
    banner_title = models.CharField(max_length=100)
    banner_desc = models.TextField()
    banner_right_desc = models.TextField()
    read_more_desc = models.TextField()

    class Meta:
        db_table = 'vg_banner'

class About_Details(models.Model):
    ICON_CHOICES = (
    ('fa-align-left','align-left'),('fa-align-right','align-right'),('fa-amazon','amazon'),('fa-ambulance','ambulance'),('fa-anchor','anchor'),('fa-android','android'),('fa-angellist','angellist'),('fa-angle-double-down','angle-double-down'),('fa-angle-double-left','angle-double-left'),('fa-angle-double-right','angle-double-right'),('fa-angle-double-up','angle-double-up'),('fa-angle-left','angle-left'),('fa-angle-right','angle-right'),('fa-angle-up','angle-up'),('fa-apple','apple'),('fa-archive','archive'),('fa-area-chart','area-chart'),('fa-arrow-circle-down','arrow-circle-down'),('fa-arrow-circle-left','arrow-circle-left'),('fa-arrow-circle-o-down','arrow-circle-o-down'),('fa-arrow-circle-o-left','arrow-circle-o-left'),('fa-arrow-circle-o-right','arrow-circle-o-right'),('fa-arrow-circle-o-up','arrow-circle-o-up'),('fa-arrow-circle-right','arrow-circle-right'),('fa-arrow-circle-up','arrow-circle-up'),('fa-arrow-down','arrow-down'),('fa-arrow-left','arrow-left'),('fa-arrow-right','arrow-right'),('fa-arrow-up','arrow-up'),('fa-arrows','arrows'),('fa-arrows-alt','arrows-alt'),('fa-arrows-h','arrows-h'),('fa-arrows-v','arrows-v'),('fa-asterisk','asterisk'),('fa-at','at'),('fa-automobile','automobile'),('fa-backward','backward'),('fa-balance-scale','balance-scale'),('fa-ban','ban'),('fa-bank','bank'),('fa-bar-chart','bar-chart'),('fa-bar-chart-o','bar-chart-o'),('fa-battery-full','battery-full'),('fa-behance','behance'),('fa-behance-square','behance-square'),('fa-bell','bell'),('fa-bell-o','bell-o'),('fa-bell-slash','bell-slash'),('fa-bell-slash-o','bell-slash-o'),('fa-bicycle','bicycle'),('fa-binoculars','binoculars'),('fa-birthday-cake','birthday-cake'),('fa-bitbucket','bitbucket'),('fa-bitbucket-square','bitbucket-square'),('fa-bitcoin','bitcoin'),('fa-black-tie','black-tie'),('fa-bold','bold'),('fa-bolt','bolt'),('fa-bomb','bomb'),('fa-book','book'),('fa-bookmark','bookmark'),('fa-bookmark-o','bookmark-o'),('fa-briefcase','briefcase'),('fa-btc','btc'),('fa-bug','bug'),('fa-building','building'),('fa-building-o','building-o'),('fa-bullhorn','bullhorn'),('fa-bullseye','bullseye'),('fa-bus','bus'),('fa-cab','cab'),('fa-calendar','calendar'),('fa-camera','camera'),('fa-car','car'),('fa-caret-up','caret-up'),('fa-cart-plus','cart-plus'),('fa-cc','cc'),('fa-cc-amex','cc-amex'),('fa-cc-jcb','cc-jcb'),('fa-cc-paypal','cc-paypal'),('fa-cc-stripe','cc-stripe'),('fa-cc-visa','cc-visa'),('fa-chain','chain'),('fa-check','check'),('fa-chevron-left','chevron-left'),('fa-chevron-right','chevron-right'),('fa-chevron-up','chevron-up'),('fa-child','child'),('fa-chrome','chrome'),('fa-circle','circle'),('fa-circle-o','circle-o'),('fa-circle-o-notch','circle-o-notch'),('fa-circle-thin','circle-thin'),('fa-clipboard','clipboard'),('fa-clock-o','clock-o'),('fa-clone','clone'),('fa-close','close'),('fa-cloud','cloud'),('fa-cloud-download','cloud-download'),('fa-cloud-upload','cloud-upload'),('fa-cny','cny'),('fa-code','code'),('fa-code-fork','code-fork'),('fa-codepen','codepen'),('fa-coffee','coffee'),('fa-cog','cog'),('fa-cogs','cogs'),('fa-columns','columns'),('fa-comment','comment'),('fa-comment-o','comment-o'),('fa-commenting','commenting'),('fa-commenting-o','commenting-o'),('fa-comments','comments'),('fa-comments-o','comments-o'),('fa-compass','compass'),('fa-compress','compress'),('fa-connectdevelop','connectdevelop'),('fa-contao','contao'),('fa-copy','copy'),('fa-copyright','copyright'),('fa-creative-commons','creative-commons'),('fa-credit-card','credit-card'),('fa-crop','crop'),('fa-crosshairs','crosshairs'),('fa-css3','css3'),('fa-cube','cube'),('fa-cubes','cubes'),('fa-cut','cut'),('fa-cutlery','cutlery'),('fa-dashboard','dashboard'),('fa-dashcube','dashcube'),('fa-database','database'),('fa-dedent','dedent'),('fa-delicious','delicious'),('fa-desktop','desktop'),('fa-deviantart','deviantart'),('fa-diamond','diamond'),('fa-digg','digg'),('fa-dollar','dollar'),('fa-download','download'),('fa-dribbble','dribbble'),('fa-dropbox','dropbox'),('fa-drupal','drupal'),('fa-edit','edit'),('fa-eject','eject'),('fa-ellipsis-h','ellipsis-h'),('fa-ellipsis-v','ellipsis-v'),('fa-empire','empire'),('fa-envelope','envelope'),('fa-envelope-o','envelope-o'),('fa-eur','eur'),('fa-euro','euro'),('fa-exchange','exchange'),('fa-exclamation','exclamation'),('fa-exclamation-circle','exclamation-circle'),('fa-exclamation-triangle','exclamation-triangle'),('fa-expand','expand'),('fa-expeditedssl','expeditedssl'),('fa-external-link','external-link'),('fa-external-link-square','external-link-square'),('fa-eye','eye'),('fa-eye-slash','eye-slash'),('fa-eyedropper','eyedropper'),('fa-facebook','facebook'),('fa-facebook-f','facebook-f'),('fa-facebook-official','facebook-official'),('fa-facebook-square','facebook-square'),('fa-fast-backward','fast-backward'),('fa-fast-forward','fast-forward'),('fa-fax','fax'),('fa-feed','feed'),('fa-female','female'),('fa-fighter-jet','fighter-jet'),('fa-file','file'),('fa-file-archive-o','file-archive-o'),('fa-file-audio-o','file-audio-o'),('fa-file-code-o','file-code-o'),('fa-file-excel-o','file-excel-o'),('fa-file-image-o','file-image-o'),('fa-file-movie-o','file-movie-o'),('fa-file-o','file-o'),('fa-file-pdf-o','file-pdf-o'),('fa-file-photo-o','file-photo-o'),('fa-file-picture-o','file-picture-o'),('fa-file-powerpoint-o','file-powerpoint-o'),('fa-file-sound-o','file-sound-o'),('fa-file-text','file-text'),('fa-file-text-o','file-text-o'),('fa-file-video-o','file-video-o'),('fa-file-word-o','file-word-o'),('fa-file-zip-o','file-zip-o'),('fa-files-o','files-o'),('fa-film','film'),('fa-filter','filter'),('fa-fire','fire'),('fa-fire-extinguisher','fire-extinguisher'),('fa-firefox','firefox'),('fa-flag','flag'),('fa-flag-checkered','flag-checkered'),('fa-flag-o','flag-o'),('fa-flash','flash'),('fa-flask','flask'),('fa-flickr','flickr'),('fa-floppy-o','floppy-o'),('fa-folder','folder'),('fa-folder-o','folder-o'),('fa-folder-open','folder-open'),('fa-folder-open-o','folder-open-o'),('fa-font','font'),('fa-fonticons','fonticons'),('fa-forumbee','forumbee'),('fa-forward','forward'),('fa-foursquare','foursquare'),('fa-frown-o','frown-o'),('fa-futbol-o','futbol-o'),('fa-gamepad','gamepad'),('fa-gavel','gavel'),('fa-gbp','gbp'),('fa-ge','ge'),('fa-gear','gear'),('fa-gears','gears'),('fa-genderless','genderless'),('fa-get-pocket','get-pocket'),('fa-gg','gg'),('fa-gg-circle','gg-circle'),('fa-gift','gift'),('fa-git','git'),('fa-git-square','git-square'),('fa-github','github'),('fa-github-alt','github-alt'),('fa-github-square','github-square'),('fa-gittip','gittip'),('fa-glass','glass'),('fa-globe','globe'),('fa-google','google'),('fa-google-plus','google-plus'),('fa-google-plus-square','google-plus-square'),('fa-google-wallet','google-wallet'),('fa-graduation-cap','graduation-cap'),('fa-gratipay','gratipay'),('fa-group','group'),('fa-h-square','h-square'),('fa-hacker-news','hacker-news'),('fa-hand-grab-o','hand-grab-o'),('fa-hand-lizard-o','hand-lizard-o'),('fa-hand-o-down','hand-o-down'),('fa-hand-o-left','hand-o-left'),('fa-hand-o-right','hand-o-right'),('fa-hand-o-up','hand-o-up'),('fa-hand-paper-o','hand-paper-o'),('fa-hand-peace-o','hand-peace-o'),('fa-hand-pointer-o','hand-pointer-o'),('fa-hand-rock-o','hand-rock-o'),('fa-hand-scissors-o','hand-scissors-o'),('fa-hand-spock-o','hand-spock-o'),('fa-hand-stop-o','hand-stop-o'),('fa-hdd-o','hdd-o'),('fa-header','header'),('fa-headphones','headphones'),('fa-heart','heart'),('fa-heart-o','heart-o'),('fa-heartbeat','heartbeat'),('fa-history','history'),('fa-home','home'),('fa-hospital-o','hospital-o'),('fa-hotel','hotel'),('fa-hourglass','hourglass'),('fa-hourglass-1','hourglass-1'),('fa-hourglass-2','hourglass-2'),('fa-hourglass-3','hourglass-3'),('fa-hourglass-end','hourglass-end'),('fa-hourglass-half','hourglass-half'),('fa-hourglass-o','hourglass-o'),('fa-hourglass-start','hourglass-start'),('fa-houzz','houzz'),('fa-html5','html5'),('fa-i-cursor','i-cursor'),('fa-ils','ils'),('fa-image','image'),('fa-inbox','inbox'),('fa-indent','indent'),('fa-industry','industry'),('fa-info','info'),('fa-info-circle','info-circle'),('fa-inr','inr'),('fa-instagram','instagram'),('fa-institution','institution'),('fa-internet-explorer','internet-explorer'),('fa-intersex','intersex'),('fa-ioxhost','ioxhost'),('fa-italic','italic'),('fa-joomla','joomla'),('fa-jpy','jpy'),('fa-jsfiddle','jsfiddle'),('fa-key','key'),('fa-keyboard-o','keyboard-o'),('fa-krw','krw'),('fa-language','language'),('fa-laptop','laptop'),('fa-lastfm','lastfm'),('fa-lastfm-square','lastfm-square'),('fa-leaf','leaf'),('fa-leanpub','leanpub'),('fa-legal','legal'),('fa-lemon-o','lemon-o'),('fa-level-down','level-down'),('fa-level-up','level-up'),('fa-life-bouy','life-bouy'),('fa-life-buoy','life-buoy'),('fa-life-ring','life-ring'),('fa-life-saver','life-saver'),('fa-lightbulb-o','lightbulb-o'),('fa-line-chart','line-chart'),('fa-link','link'),('fa-linkedin','linkedin'),('fa-linkedin-square','linkedin-square'),('fa-linux','linux'),('fa-list','list'),('fa-list-alt','list-alt'),('fa-list-ol','list-ol'),('fa-list-ul','list-ul'),('fa-location-arrow','location-arrow'),('fa-lock','lock'),('fa-long-arrow-down','long-arrow-down'),('fa-long-arrow-left','long-arrow-left'),('fa-long-arrow-right','long-arrow-right'),('fa-long-arrow-up','long-arrow-up'),('fa-magic','magic'),('fa-magnet','magnet'),('fa-mars-stroke-v','mars-stroke-v'),('fa-maxcdn','maxcdn'),('fa-meanpath','meanpath'),('fa-medium','medium'),('fa-medkit','medkit'),('fa-meh-o','meh-o'),('fa-mercury','mercury'),('fa-microphone','microphone'),('fa-mobile','mobile'),('fa-motorcycle','motorcycle'),('fa-mouse-pointer','mouse-pointer'),('fa-music','music'),('fa-navicon','navicon'),('fa-neuter','neuter'),('fa-newspaper-o','newspaper-o'),('fa-opencart','opencart'),('fa-openid','openid'),('fa-opera','opera'),('fa-outdent','outdent'),('fa-pagelines','pagelines'),('fa-paper-plane-o','paper-plane-o'),('fa-paperclip','paperclip'),('fa-paragraph','paragraph'),('fa-paste','paste'),
    ('fa-pause','pause'),('fa-paw','paw'),('fa-paypal','paypal'),('fa-pencil','pencil'),('fa-pencil-square-o','pencil-square-o'),('fa-phone','phone'),('fa-photo','photo'),('fa-picture-o','picture-o'),('fa-pie-chart','pie-chart'),('fa-pied-piper','pied-piper'),('fa-pied-piper-alt','pied-piper-alt'),('fa-pinterest','pinterest'),('fa-pinterest-p','pinterest-p'),('fa-pinterest-square','pinterest-square'),('fa-plane','plane'),('fa-play','play'),('fa-play-circle','play-circle'),('fa-play-circle-o','play-circle-o'),('fa-plug','plug'),('fa-plus','plus'),('fa-plus-circle','plus-circle'),('fa-plus-square','plus-square'),('fa-plus-square-o','plus-square-o'),('fa-power-off','power-off'),('fa-print','print'),('fa-puzzle-piece','puzzle-piece'),('fa-qq','qq'),('fa-qrcode','qrcode'),('fa-question','question'),('fa-question-circle','question-circle'),('fa-quote-left','quote-left'),('fa-quote-right','quote-right'),('fa-ra','ra'),('fa-random','random'),('fa-rebel','rebel'),('fa-recycle','recycle'),('fa-reddit','reddit'),('fa-reddit-square','reddit-square'),('fa-refresh','refresh'),('fa-registered','registered'),('fa-remove','remove'),('fa-renren','renren'),('fa-reorder','reorder'),('fa-repeat','repeat'),('fa-reply','reply'),('fa-reply-all','reply-all'),('fa-retweet','retweet'),('fa-rmb','rmb'),('fa-road','road'),('fa-rocket','rocket'),('fa-rotate-left','rotate-left'),('fa-rotate-right','rotate-right'),('fa-rouble','rouble'),('fa-rss','rss'),('fa-rss-square','rss-square'),('fa-rub','rub'),('fa-ruble','ruble'),('fa-rupee','rupee'),('fa-safari','safari'),('fa-sliders','sliders'),('fa-slideshare','slideshare'),('fa-smile-o','smile-o'),('fa-sort-asc','sort-asc'),('fa-sort-desc','sort-desc'),('fa-sort-down','sort-down'),('fa-spinner','spinner'),('fa-spoon','spoon'),('fa-spotify','spotify'),('fa-square','square'),('fa-square-o','square-o'),('fa-star','star'),('fa-star-half','star-half'),('fa-stop','stop'),('fa-subscript','subscript'),('fa-tablet','tablet'),('fa-tachometer','tachometer'),('fa-tag','tag'),('fa-tags','tags')
     )
      
    about_title_name = models.CharField(max_length=30)
    about_image = models.ImageField(upload_to='media')
    about_desc = models.TextField(max_length=200)

    # Side service 1
    about_service_type = models.CharField(max_length=30)
    about_service_icon = models.CharField(max_length=200,choices = ICON_CHOICES)
    about_service_desc = models.TextField(max_length=200)

    #Side Service 2
    about_service_type1 = models.CharField(max_length=30)
    about_service_icon1 = models.CharField(max_length=200,choices = ICON_CHOICES)
    about_service_desc1 = models.TextField(max_length=200)

    #Side Service 3
    about_service_type2 = models.CharField(max_length=30)
    about_service_icon2 = models.CharField(max_length=200,choices = ICON_CHOICES)
    about_service_desc2 = models.TextField(max_length=200)
class ProfessionTeam(models.Model):
    """
    model class for handling contact header informations

    """
    avatar = models.ImageField(upload_to="media")
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=25)
    description = models.TextField(null=True)
    phone_number = models.BigIntegerField()
    country_code = models.CharField(max_length=6)
    contact_email = models.EmailField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    insta_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'vg_professional_teaml'


class ContactHeader(models.Model):
    """
    model class for handling contact header informations

    """
    phone_number = models.BigIntegerField()
    country_code = models.CharField(max_length=6)
    contact_email = models.EmailField()
    address = models.CharField(max_length=100,null=True,blank=True)
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    insta_url = models.URLField()
    linkedin_url = models.URLField()
    google_map_url = models.CharField(max_length=500,null=True,blank=True)


    class Meta:
        db_table = 'vg_contact_header'


class ServicesOffered(models.Model):
    """
    service model to store the type of service offered by the company

    """
    ICON_CHOICES = (
    ('fa-align-left','align-left'),('fa-align-right','align-right'),('fa-amazon','amazon'),('fa-ambulance','ambulance'),('fa-anchor','anchor'),('fa-android','android'),('fa-angellist','angellist'),('fa-angle-double-down','angle-double-down'),('fa-angle-double-left','angle-double-left'),('fa-angle-double-right','angle-double-right'),('fa-angle-double-up','angle-double-up'),('fa-angle-left','angle-left'),('fa-angle-right','angle-right'),('fa-angle-up','angle-up'),('fa-apple','apple'),('fa-archive','archive'),('fa-area-chart','area-chart'),('fa-arrow-circle-down','arrow-circle-down'),('fa-arrow-circle-left','arrow-circle-left'),('fa-arrow-circle-o-down','arrow-circle-o-down'),('fa-arrow-circle-o-left','arrow-circle-o-left'),('fa-arrow-circle-o-right','arrow-circle-o-right'),('fa-arrow-circle-o-up','arrow-circle-o-up'),('fa-arrow-circle-right','arrow-circle-right'),('fa-arrow-circle-up','arrow-circle-up'),('fa-arrow-down','arrow-down'),('fa-arrow-left','arrow-left'),('fa-arrow-right','arrow-right'),('fa-arrow-up','arrow-up'),('fa-arrows','arrows'),('fa-arrows-alt','arrows-alt'),('fa-arrows-h','arrows-h'),('fa-arrows-v','arrows-v'),('fa-asterisk','asterisk'),('fa-at','at'),('fa-automobile','automobile'),('fa-backward','backward'),('fa-balance-scale','balance-scale'),('fa-ban','ban'),('fa-bank','bank'),('fa-bar-chart','bar-chart'),('fa-bar-chart-o','bar-chart-o'),('fa-battery-full','battery-full'),('fa-behance','behance'),('fa-behance-square','behance-square'),('fa-bell','bell'),('fa-bell-o','bell-o'),('fa-bell-slash','bell-slash'),('fa-bell-slash-o','bell-slash-o'),('fa-bicycle','bicycle'),('fa-binoculars','binoculars'),('fa-birthday-cake','birthday-cake'),('fa-bitbucket','bitbucket'),('fa-bitbucket-square','bitbucket-square'),('fa-bitcoin','bitcoin'),('fa-black-tie','black-tie'),('fa-bold','bold'),('fa-bolt','bolt'),('fa-bomb','bomb'),('fa-book','book'),('fa-bookmark','bookmark'),('fa-bookmark-o','bookmark-o'),('fa-briefcase','briefcase'),('fa-btc','btc'),('fa-bug','bug'),('fa-building','building'),('fa-building-o','building-o'),('fa-bullhorn','bullhorn'),('fa-bullseye','bullseye'),('fa-bus','bus'),('fa-cab','cab'),('fa-calendar','calendar'),('fa-camera','camera'),('fa-car','car'),('fa-caret-up','caret-up'),('fa-cart-plus','cart-plus'),('fa-cc','cc'),('fa-cc-amex','cc-amex'),('fa-cc-jcb','cc-jcb'),('fa-cc-paypal','cc-paypal'),('fa-cc-stripe','cc-stripe'),('fa-cc-visa','cc-visa'),('fa-chain','chain'),('fa-check','check'),('fa-chevron-left','chevron-left'),('fa-chevron-right','chevron-right'),('fa-chevron-up','chevron-up'),('fa-child','child'),('fa-chrome','chrome'),('fa-circle','circle'),('fa-circle-o','circle-o'),('fa-circle-o-notch','circle-o-notch'),('fa-circle-thin','circle-thin'),('fa-clipboard','clipboard'),('fa-clock-o','clock-o'),('fa-clone','clone'),('fa-close','close'),('fa-cloud','cloud'),('fa-cloud-download','cloud-download'),('fa-cloud-upload','cloud-upload'),('fa-cny','cny'),('fa-code','code'),('fa-code-fork','code-fork'),('fa-codepen','codepen'),('fa-coffee','coffee'),('fa-cog','cog'),('fa-cogs','cogs'),('fa-columns','columns'),('fa-comment','comment'),('fa-comment-o','comment-o'),('fa-commenting','commenting'),('fa-commenting-o','commenting-o'),('fa-comments','comments'),('fa-comments-o','comments-o'),('fa-compass','compass'),('fa-compress','compress'),('fa-connectdevelop','connectdevelop'),('fa-contao','contao'),('fa-copy','copy'),('fa-copyright','copyright'),('fa-creative-commons','creative-commons'),('fa-credit-card','credit-card'),('fa-crop','crop'),('fa-crosshairs','crosshairs'),('fa-css3','css3'),('fa-cube','cube'),('fa-cubes','cubes'),('fa-cut','cut'),('fa-cutlery','cutlery'),('fa-dashboard','dashboard'),('fa-dashcube','dashcube'),('fa-database','database'),('fa-dedent','dedent'),('fa-delicious','delicious'),('fa-desktop','desktop'),('fa-deviantart','deviantart'),('fa-diamond','diamond'),('fa-digg','digg'),('fa-dollar','dollar'),('fa-download','download'),('fa-dribbble','dribbble'),('fa-dropbox','dropbox'),('fa-drupal','drupal'),('fa-edit','edit'),('fa-eject','eject'),('fa-ellipsis-h','ellipsis-h'),('fa-ellipsis-v','ellipsis-v'),('fa-empire','empire'),('fa-envelope','envelope'),('fa-envelope-o','envelope-o'),('fa-eur','eur'),('fa-euro','euro'),('fa-exchange','exchange'),('fa-exclamation','exclamation'),('fa-exclamation-circle','exclamation-circle'),('fa-exclamation-triangle','exclamation-triangle'),('fa-expand','expand'),('fa-expeditedssl','expeditedssl'),('fa-external-link','external-link'),('fa-external-link-square','external-link-square'),('fa-eye','eye'),('fa-eye-slash','eye-slash'),('fa-eyedropper','eyedropper'),('fa-facebook','facebook'),('fa-facebook-f','facebook-f'),('fa-facebook-official','facebook-official'),('fa-facebook-square','facebook-square'),('fa-fast-backward','fast-backward'),('fa-fast-forward','fast-forward'),('fa-fax','fax'),('fa-feed','feed'),('fa-female','female'),('fa-fighter-jet','fighter-jet'),('fa-file','file'),('fa-file-archive-o','file-archive-o'),('fa-file-audio-o','file-audio-o'),('fa-file-code-o','file-code-o'),('fa-file-excel-o','file-excel-o'),('fa-file-image-o','file-image-o'),('fa-file-movie-o','file-movie-o'),('fa-file-o','file-o'),('fa-file-pdf-o','file-pdf-o'),('fa-file-photo-o','file-photo-o'),('fa-file-picture-o','file-picture-o'),('fa-file-powerpoint-o','file-powerpoint-o'),('fa-file-sound-o','file-sound-o'),('fa-file-text','file-text'),('fa-file-text-o','file-text-o'),('fa-file-video-o','file-video-o'),('fa-file-word-o','file-word-o'),('fa-file-zip-o','file-zip-o'),('fa-files-o','files-o'),('fa-film','film'),('fa-filter','filter'),('fa-fire','fire'),('fa-fire-extinguisher','fire-extinguisher'),('fa-firefox','firefox'),('fa-flag','flag'),('fa-flag-checkered','flag-checkered'),('fa-flag-o','flag-o'),('fa-flash','flash'),('fa-flask','flask'),('fa-flickr','flickr'),('fa-floppy-o','floppy-o'),('fa-folder','folder'),('fa-folder-o','folder-o'),('fa-folder-open','folder-open'),('fa-folder-open-o','folder-open-o'),('fa-font','font'),('fa-fonticons','fonticons'),('fa-forumbee','forumbee'),('fa-forward','forward'),('fa-foursquare','foursquare'),('fa-frown-o','frown-o'),('fa-futbol-o','futbol-o'),('fa-gamepad','gamepad'),('fa-gavel','gavel'),('fa-gbp','gbp'),('fa-ge','ge'),('fa-gear','gear'),('fa-gears','gears'),('fa-genderless','genderless'),('fa-get-pocket','get-pocket'),('fa-gg','gg'),('fa-gg-circle','gg-circle'),('fa-gift','gift'),('fa-git','git'),('fa-git-square','git-square'),('fa-github','github'),('fa-github-alt','github-alt'),('fa-github-square','github-square'),('fa-gittip','gittip'),('fa-glass','glass'),('fa-globe','globe'),('fa-google','google'),('fa-google-plus','google-plus'),('fa-google-plus-square','google-plus-square'),('fa-google-wallet','google-wallet'),('fa-graduation-cap','graduation-cap'),('fa-gratipay','gratipay'),('fa-group','group'),('fa-h-square','h-square'),('fa-hacker-news','hacker-news'),('fa-hand-grab-o','hand-grab-o'),('fa-hand-lizard-o','hand-lizard-o'),('fa-hand-o-down','hand-o-down'),('fa-hand-o-left','hand-o-left'),('fa-hand-o-right','hand-o-right'),('fa-hand-o-up','hand-o-up'),('fa-hand-paper-o','hand-paper-o'),('fa-hand-peace-o','hand-peace-o'),('fa-hand-pointer-o','hand-pointer-o'),('fa-hand-rock-o','hand-rock-o'),('fa-hand-scissors-o','hand-scissors-o'),('fa-hand-spock-o','hand-spock-o'),('fa-hand-stop-o','hand-stop-o'),('fa-hdd-o','hdd-o'),('fa-header','header'),('fa-headphones','headphones'),('fa-heart','heart'),('fa-heart-o','heart-o'),('fa-heartbeat','heartbeat'),('fa-history','history'),('fa-home','home'),('fa-hospital-o','hospital-o'),('fa-hotel','hotel'),('fa-hourglass','hourglass'),('fa-hourglass-1','hourglass-1'),('fa-hourglass-2','hourglass-2'),('fa-hourglass-3','hourglass-3'),('fa-hourglass-end','hourglass-end'),('fa-hourglass-half','hourglass-half'),('fa-hourglass-o','hourglass-o'),('fa-hourglass-start','hourglass-start'),('fa-houzz','houzz'),('fa-html5','html5'),('fa-i-cursor','i-cursor'),('fa-ils','ils'),('fa-image','image'),('fa-inbox','inbox'),('fa-indent','indent'),('fa-industry','industry'),('fa-info','info'),('fa-info-circle','info-circle'),('fa-inr','inr'),('fa-instagram','instagram'),('fa-institution','institution'),('fa-internet-explorer','internet-explorer'),('fa-intersex','intersex'),('fa-ioxhost','ioxhost'),('fa-italic','italic'),('fa-joomla','joomla'),('fa-jpy','jpy'),('fa-jsfiddle','jsfiddle'),('fa-key','key'),('fa-keyboard-o','keyboard-o'),('fa-krw','krw'),('fa-language','language'),('fa-laptop','laptop'),('fa-lastfm','lastfm'),('fa-lastfm-square','lastfm-square'),('fa-leaf','leaf'),('fa-leanpub','leanpub'),('fa-legal','legal'),('fa-lemon-o','lemon-o'),('fa-level-down','level-down'),('fa-level-up','level-up'),('fa-life-bouy','life-bouy'),('fa-life-buoy','life-buoy'),('fa-life-ring','life-ring'),('fa-life-saver','life-saver'),('fa-lightbulb-o','lightbulb-o'),('fa-line-chart','line-chart'),('fa-link','link'),('fa-linkedin','linkedin'),('fa-linkedin-square','linkedin-square'),('fa-linux','linux'),('fa-list','list'),('fa-list-alt','list-alt'),('fa-list-ol','list-ol'),('fa-list-ul','list-ul'),('fa-location-arrow','location-arrow'),('fa-lock','lock'),('fa-long-arrow-down','long-arrow-down'),('fa-long-arrow-left','long-arrow-left'),('fa-long-arrow-right','long-arrow-right'),('fa-long-arrow-up','long-arrow-up'),('fa-magic','magic'),('fa-magnet','magnet'),('fa-mars-stroke-v','mars-stroke-v'),('fa-maxcdn','maxcdn'),('fa-meanpath','meanpath'),('fa-medium','medium'),('fa-medkit','medkit'),('fa-meh-o','meh-o'),('fa-mercury','mercury'),('fa-microphone','microphone'),('fa-mobile','mobile'),('fa-motorcycle','motorcycle'),('fa-mouse-pointer','mouse-pointer'),('fa-music','music'),('fa-navicon','navicon'),('fa-neuter','neuter'),('fa-newspaper-o','newspaper-o'),('fa-opencart','opencart'),('fa-openid','openid'),('fa-opera','opera'),('fa-outdent','outdent'),('fa-pagelines','pagelines'),('fa-paper-plane-o','paper-plane-o'),('fa-paperclip','paperclip'),('fa-paragraph','paragraph'),('fa-paste','paste'),
    ('fa-pause','pause'),('fa-paw','paw'),('fa-paypal','paypal'),('fa-pencil','pencil'),('fa-pencil-square-o','pencil-square-o'),('fa-phone','phone'),('fa-photo','photo'),('fa-picture-o','picture-o'),('fa-pie-chart','pie-chart'),('fa-pied-piper','pied-piper'),('fa-pied-piper-alt','pied-piper-alt'),('fa-pinterest','pinterest'),('fa-pinterest-p','pinterest-p'),('fa-pinterest-square','pinterest-square'),('fa-plane','plane'),('fa-play','play'),('fa-play-circle','play-circle'),('fa-play-circle-o','play-circle-o'),('fa-plug','plug'),('fa-plus','plus'),('fa-plus-circle','plus-circle'),('fa-plus-square','plus-square'),('fa-plus-square-o','plus-square-o'),('fa-power-off','power-off'),('fa-print','print'),('fa-puzzle-piece','puzzle-piece'),('fa-qq','qq'),('fa-qrcode','qrcode'),('fa-question','question'),('fa-question-circle','question-circle'),('fa-quote-left','quote-left'),('fa-quote-right','quote-right'),('fa-ra','ra'),('fa-random','random'),('fa-rebel','rebel'),('fa-recycle','recycle'),('fa-reddit','reddit'),('fa-reddit-square','reddit-square'),('fa-refresh','refresh'),('fa-registered','registered'),('fa-remove','remove'),('fa-renren','renren'),('fa-reorder','reorder'),('fa-repeat','repeat'),('fa-reply','reply'),('fa-reply-all','reply-all'),('fa-retweet','retweet'),('fa-rmb','rmb'),('fa-road','road'),('fa-rocket','rocket'),('fa-rotate-left','rotate-left'),('fa-rotate-right','rotate-right'),('fa-rouble','rouble'),('fa-rss','rss'),('fa-rss-square','rss-square'),('fa-rub','rub'),('fa-ruble','ruble'),('fa-rupee','rupee'),('fa-safari','safari'),('fa-sliders','sliders'),('fa-slideshare','slideshare'),('fa-smile-o','smile-o'),('fa-sort-asc','sort-asc'),('fa-sort-desc','sort-desc'),('fa-sort-down','sort-down'),('fa-spinner','spinner'),('fa-spoon','spoon'),('fa-spotify','spotify'),('fa-square','square'),('fa-square-o','square-o'),('fa-star','star'),('fa-star-half','star-half'),('fa-stop','stop'),('fa-subscript','subscript'),('fa-tablet','tablet'),('fa-tachometer','tachometer'),('fa-tag','tag'),('fa-tags','tags')
     )

    service_name = models.CharField(max_length=30)
    service_desc = models.TextField()
    service_image = models.ImageField(upload_to='media')
    service_icon = models.CharField(max_length=200,choices = ICON_CHOICES)

    class Meta:
        db_table = 'vg_service_offered'


class HappyClients(models.Model):
    client_name = models.CharField(max_length=50)
    designation = models.CharField(max_length=25)
    avatar = models.ImageField(upload_to='media')
    rating = models.IntegerField()
    description = models.TextField()

    class Meta:
        db_table = 'vg_happy_clients'


class ConsultingCustomer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=255)
    number = models.CharField(max_length=20)
    message = models.TextField(null=True,blank=True)

    class Meta:
        db_table = 'vg_consulting_clients'


class AboutUs(models.Model):
    title = models.CharField(max_length=25)
    banner = models.ImageField(upload_to = "media",null=True)
    heading = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    per_mangemt = models.IntegerField()
    per_marketing = models.IntegerField()
    per_stratergy = models.IntegerField()
    per_deployment = models.IntegerField()

    class Meta:
        db_table = "vg_about_us"


class SubscriptionPlans(models.Model):
    plan_name = models.CharField(max_length=25)
    price = models.FloatField()
    currency = models.CharField(max_length=4)
    period = models.CharField(max_length = 15,default="month")
    color_code = models.CharField(max_length=20,default="#585858")
    email_suppport = models.CharField(max_length=50)
    storage_suppport = models.CharField(max_length=50)
    website_suppport = models.CharField(max_length=50)
    bandwidth_suppport = models.CharField(max_length=50)
    customer_suppport = models.CharField(max_length=50)

    class Meta:
        db_table = 'vg_subscription_plan'
    
class GalleryContent(models.Model):
    """
    model content file management 

    """
    CATEGORY = (
        (0,'ALL'),
        (1,'Finance'),
        (2,'Business'),
        (3,'Strategy'),
        (4,'Development')
    )
    image = models.ImageField(upload_to = "media")
    alt_text = models.CharField(max_length = 20)
    image_category = models.SmallIntegerField(choices=CATEGORY)
    


    #Our Statistics



class OurStatistics(models.Model):
    """
    service model to store the type of service offered by the company

    """
    ICON_CHOICES = (
    ('fa-align-left','align-left'),('fa-align-right','align-right'),('fa-amazon','amazon'),('fa-ambulance','ambulance'),('fa-anchor','anchor'),('fa-android','android'),('fa-angellist','angellist'),('fa-angle-double-down','angle-double-down'),('fa-angle-double-left','angle-double-left'),('fa-angle-double-right','angle-double-right'),('fa-angle-double-up','angle-double-up'),('fa-angle-left','angle-left'),('fa-angle-right','angle-right'),('fa-angle-up','angle-up'),('fa-apple','apple'),('fa-archive','archive'),('fa-area-chart','area-chart'),('fa-arrow-circle-down','arrow-circle-down'),('fa-arrow-circle-left','arrow-circle-left'),('fa-arrow-circle-o-down','arrow-circle-o-down'),('fa-arrow-circle-o-left','arrow-circle-o-left'),('fa-arrow-circle-o-right','arrow-circle-o-right'),('fa-arrow-circle-o-up','arrow-circle-o-up'),('fa-arrow-circle-right','arrow-circle-right'),('fa-arrow-circle-up','arrow-circle-up'),('fa-arrow-down','arrow-down'),('fa-arrow-left','arrow-left'),('fa-arrow-right','arrow-right'),('fa-arrow-up','arrow-up'),('fa-arrows','arrows'),('fa-arrows-alt','arrows-alt'),('fa-arrows-h','arrows-h'),('fa-arrows-v','arrows-v'),('fa-asterisk','asterisk'),('fa-at','at'),('fa-automobile','automobile'),('fa-backward','backward'),('fa-balance-scale','balance-scale'),('fa-ban','ban'),('fa-bank','bank'),('fa-bar-chart','bar-chart'),('fa-bar-chart-o','bar-chart-o'),('fa-battery-full','battery-full'),('fa-behance','behance'),('fa-behance-square','behance-square'),('fa-bell','bell'),('fa-bell-o','bell-o'),('fa-bell-slash','bell-slash'),('fa-bell-slash-o','bell-slash-o'),('fa-bicycle','bicycle'),('fa-binoculars','binoculars'),('fa-birthday-cake','birthday-cake'),('fa-bitbucket','bitbucket'),('fa-bitbucket-square','bitbucket-square'),('fa-bitcoin','bitcoin'),('fa-black-tie','black-tie'),('fa-bold','bold'),('fa-bolt','bolt'),('fa-bomb','bomb'),('fa-book','book'),('fa-bookmark','bookmark'),('fa-bookmark-o','bookmark-o'),('fa-briefcase','briefcase'),('fa-btc','btc'),('fa-bug','bug'),('fa-building','building'),('fa-building-o','building-o'),('fa-bullhorn','bullhorn'),('fa-bullseye','bullseye'),('fa-bus','bus'),('fa-cab','cab'),('fa-calendar','calendar'),('fa-camera','camera'),('fa-car','car'),('fa-caret-up','caret-up'),('fa-cart-plus','cart-plus'),('fa-cc','cc'),('fa-cc-amex','cc-amex'),('fa-cc-jcb','cc-jcb'),('fa-cc-paypal','cc-paypal'),('fa-cc-stripe','cc-stripe'),('fa-cc-visa','cc-visa'),('fa-chain','chain'),('fa-check','check'),('fa-chevron-left','chevron-left'),('fa-chevron-right','chevron-right'),('fa-chevron-up','chevron-up'),('fa-child','child'),('fa-chrome','chrome'),('fa-circle','circle'),('fa-circle-o','circle-o'),('fa-circle-o-notch','circle-o-notch'),('fa-circle-thin','circle-thin'),('fa-clipboard','clipboard'),('fa-clock-o','clock-o'),('fa-clone','clone'),('fa-close','close'),('fa-cloud','cloud'),('fa-cloud-download','cloud-download'),('fa-cloud-upload','cloud-upload'),('fa-cny','cny'),('fa-code','code'),('fa-code-fork','code-fork'),('fa-codepen','codepen'),('fa-coffee','coffee'),('fa-cog','cog'),('fa-cogs','cogs'),('fa-columns','columns'),('fa-comment','comment'),('fa-comment-o','comment-o'),('fa-commenting','commenting'),('fa-commenting-o','commenting-o'),('fa-comments','comments'),('fa-comments-o','comments-o'),('fa-compass','compass'),('fa-compress','compress'),('fa-connectdevelop','connectdevelop'),('fa-contao','contao'),('fa-copy','copy'),('fa-copyright','copyright'),('fa-creative-commons','creative-commons'),('fa-credit-card','credit-card'),('fa-crop','crop'),('fa-crosshairs','crosshairs'),('fa-css3','css3'),('fa-cube','cube'),('fa-cubes','cubes'),('fa-cut','cut'),('fa-cutlery','cutlery'),('fa-dashboard','dashboard'),('fa-dashcube','dashcube'),('fa-database','database'),('fa-dedent','dedent'),('fa-delicious','delicious'),('fa-desktop','desktop'),('fa-deviantart','deviantart'),('fa-diamond','diamond'),('fa-digg','digg'),('fa-dollar','dollar'),('fa-download','download'),('fa-dribbble','dribbble'),('fa-dropbox','dropbox'),('fa-drupal','drupal'),('fa-edit','edit'),('fa-eject','eject'),('fa-ellipsis-h','ellipsis-h'),('fa-ellipsis-v','ellipsis-v'),('fa-empire','empire'),('fa-envelope','envelope'),('fa-envelope-o','envelope-o'),('fa-eur','eur'),('fa-euro','euro'),('fa-exchange','exchange'),('fa-exclamation','exclamation'),('fa-exclamation-circle','exclamation-circle'),('fa-exclamation-triangle','exclamation-triangle'),('fa-expand','expand'),('fa-expeditedssl','expeditedssl'),('fa-external-link','external-link'),('fa-external-link-square','external-link-square'),('fa-eye','eye'),('fa-eye-slash','eye-slash'),('fa-eyedropper','eyedropper'),('fa-facebook','facebook'),('fa-facebook-f','facebook-f'),('fa-facebook-official','facebook-official'),('fa-facebook-square','facebook-square'),('fa-fast-backward','fast-backward'),('fa-fast-forward','fast-forward'),('fa-fax','fax'),('fa-feed','feed'),('fa-female','female'),('fa-fighter-jet','fighter-jet'),('fa-file','file'),('fa-file-archive-o','file-archive-o'),('fa-file-audio-o','file-audio-o'),('fa-file-code-o','file-code-o'),('fa-file-excel-o','file-excel-o'),('fa-file-image-o','file-image-o'),('fa-file-movie-o','file-movie-o'),('fa-file-o','file-o'),('fa-file-pdf-o','file-pdf-o'),('fa-file-photo-o','file-photo-o'),('fa-file-picture-o','file-picture-o'),('fa-file-powerpoint-o','file-powerpoint-o'),('fa-file-sound-o','file-sound-o'),('fa-file-text','file-text'),('fa-file-text-o','file-text-o'),('fa-file-video-o','file-video-o'),('fa-file-word-o','file-word-o'),('fa-file-zip-o','file-zip-o'),('fa-files-o','files-o'),('fa-film','film'),('fa-filter','filter'),('fa-fire','fire'),('fa-fire-extinguisher','fire-extinguisher'),('fa-firefox','firefox'),('fa-flag','flag'),('fa-flag-checkered','flag-checkered'),('fa-flag-o','flag-o'),('fa-flash','flash'),('fa-flask','flask'),('fa-flickr','flickr'),('fa-floppy-o','floppy-o'),('fa-folder','folder'),('fa-folder-o','folder-o'),('fa-folder-open','folder-open'),('fa-folder-open-o','folder-open-o'),('fa-font','font'),('fa-fonticons','fonticons'),('fa-forumbee','forumbee'),('fa-forward','forward'),('fa-foursquare','foursquare'),('fa-frown-o','frown-o'),('fa-futbol-o','futbol-o'),('fa-gamepad','gamepad'),('fa-gavel','gavel'),('fa-gbp','gbp'),('fa-ge','ge'),('fa-gear','gear'),('fa-gears','gears'),('fa-genderless','genderless'),('fa-get-pocket','get-pocket'),('fa-gg','gg'),('fa-gg-circle','gg-circle'),('fa-gift','gift'),('fa-git','git'),('fa-git-square','git-square'),('fa-github','github'),('fa-github-alt','github-alt'),('fa-github-square','github-square'),('fa-gittip','gittip'),('fa-glass','glass'),('fa-globe','globe'),('fa-google','google'),('fa-google-plus','google-plus'),('fa-google-plus-square','google-plus-square'),('fa-google-wallet','google-wallet'),('fa-graduation-cap','graduation-cap'),('fa-gratipay','gratipay'),('fa-group','group'),('fa-h-square','h-square'),('fa-hacker-news','hacker-news'),('fa-hand-grab-o','hand-grab-o'),('fa-hand-lizard-o','hand-lizard-o'),('fa-hand-o-down','hand-o-down'),('fa-hand-o-left','hand-o-left'),('fa-hand-o-right','hand-o-right'),('fa-hand-o-up','hand-o-up'),('fa-hand-paper-o','hand-paper-o'),('fa-hand-peace-o','hand-peace-o'),('fa-hand-pointer-o','hand-pointer-o'),('fa-hand-rock-o','hand-rock-o'),('fa-hand-scissors-o','hand-scissors-o'),('fa-hand-spock-o','hand-spock-o'),('fa-hand-stop-o','hand-stop-o'),('fa-hdd-o','hdd-o'),('fa-header','header'),('fa-headphones','headphones'),('fa-heart','heart'),('fa-heart-o','heart-o'),('fa-heartbeat','heartbeat'),('fa-history','history'),('fa-home','home'),('fa-hospital-o','hospital-o'),('fa-hotel','hotel'),('fa-hourglass','hourglass'),('fa-hourglass-1','hourglass-1'),('fa-hourglass-2','hourglass-2'),('fa-hourglass-3','hourglass-3'),('fa-hourglass-end','hourglass-end'),('fa-hourglass-half','hourglass-half'),('fa-hourglass-o','hourglass-o'),('fa-hourglass-start','hourglass-start'),('fa-houzz','houzz'),('fa-html5','html5'),('fa-i-cursor','i-cursor'),('fa-ils','ils'),('fa-image','image'),('fa-inbox','inbox'),('fa-indent','indent'),('fa-industry','industry'),('fa-info','info'),('fa-info-circle','info-circle'),('fa-inr','inr'),('fa-instagram','instagram'),('fa-institution','institution'),('fa-internet-explorer','internet-explorer'),('fa-intersex','intersex'),('fa-ioxhost','ioxhost'),('fa-italic','italic'),('fa-joomla','joomla'),('fa-jpy','jpy'),('fa-jsfiddle','jsfiddle'),('fa-key','key'),('fa-keyboard-o','keyboard-o'),('fa-krw','krw'),('fa-language','language'),('fa-laptop','laptop'),('fa-lastfm','lastfm'),('fa-lastfm-square','lastfm-square'),('fa-leaf','leaf'),('fa-leanpub','leanpub'),('fa-legal','legal'),('fa-lemon-o','lemon-o'),('fa-level-down','level-down'),('fa-level-up','level-up'),('fa-life-bouy','life-bouy'),('fa-life-buoy','life-buoy'),('fa-life-ring','life-ring'),('fa-life-saver','life-saver'),('fa-lightbulb-o','lightbulb-o'),('fa-line-chart','line-chart'),('fa-link','link'),('fa-linkedin','linkedin'),('fa-linkedin-square','linkedin-square'),('fa-linux','linux'),('fa-list','list'),('fa-list-alt','list-alt'),('fa-list-ol','list-ol'),('fa-list-ul','list-ul'),('fa-location-arrow','location-arrow'),('fa-lock','lock'),('fa-long-arrow-down','long-arrow-down'),('fa-long-arrow-left','long-arrow-left'),('fa-long-arrow-right','long-arrow-right'),('fa-long-arrow-up','long-arrow-up'),('fa-magic','magic'),('fa-magnet','magnet'),('fa-mars-stroke-v','mars-stroke-v'),('fa-maxcdn','maxcdn'),('fa-meanpath','meanpath'),('fa-medium','medium'),('fa-medkit','medkit'),('fa-meh-o','meh-o'),('fa-mercury','mercury'),('fa-microphone','microphone'),('fa-mobile','mobile'),('fa-motorcycle','motorcycle'),('fa-mouse-pointer','mouse-pointer'),('fa-music','music'),('fa-navicon','navicon'),('fa-neuter','neuter'),('fa-newspaper-o','newspaper-o'),('fa-opencart','opencart'),('fa-openid','openid'),('fa-opera','opera'),('fa-outdent','outdent'),('fa-pagelines','pagelines'),('fa-paper-plane-o','paper-plane-o'),('fa-paperclip','paperclip'),('fa-paragraph','paragraph'),('fa-paste','paste'),
    ('fa-pause','pause'),('fa-paw','paw'),('fa-paypal','paypal'),('fa-pencil','pencil'),('fa-pencil-square-o','pencil-square-o'),('fa-phone','phone'),('fa-photo','photo'),('fa-picture-o','picture-o'),('fa-pie-chart','pie-chart'),('fa-pied-piper','pied-piper'),('fa-pied-piper-alt','pied-piper-alt'),('fa-pinterest','pinterest'),('fa-pinterest-p','pinterest-p'),('fa-pinterest-square','pinterest-square'),('fa-plane','plane'),('fa-play','play'),('fa-play-circle','play-circle'),('fa-play-circle-o','play-circle-o'),('fa-plug','plug'),('fa-plus','plus'),('fa-plus-circle','plus-circle'),('fa-plus-square','plus-square'),('fa-plus-square-o','plus-square-o'),('fa-power-off','power-off'),('fa-print','print'),('fa-puzzle-piece','puzzle-piece'),('fa-qq','qq'),('fa-qrcode','qrcode'),('fa-question','question'),('fa-question-circle','question-circle'),('fa-quote-left','quote-left'),('fa-quote-right','quote-right'),('fa-ra','ra'),('fa-random','random'),('fa-rebel','rebel'),('fa-recycle','recycle'),('fa-reddit','reddit'),('fa-reddit-square','reddit-square'),('fa-refresh','refresh'),('fa-registered','registered'),('fa-remove','remove'),('fa-renren','renren'),('fa-reorder','reorder'),('fa-repeat','repeat'),('fa-reply','reply'),('fa-reply-all','reply-all'),('fa-retweet','retweet'),('fa-rmb','rmb'),('fa-road','road'),('fa-rocket','rocket'),('fa-rotate-left','rotate-left'),('fa-rotate-right','rotate-right'),('fa-rouble','rouble'),('fa-rss','rss'),('fa-rss-square','rss-square'),('fa-rub','rub'),('fa-ruble','ruble'),('fa-rupee','rupee'),('fa-safari','safari'),('fa-sliders','sliders'),('fa-slideshare','slideshare'),('fa-smile-o','smile-o'),('fa-sort-asc','sort-asc'),('fa-sort-desc','sort-desc'),('fa-sort-down','sort-down'),('fa-spinner','spinner'),('fa-spoon','spoon'),('fa-spotify','spotify'),('fa-square','square'),('fa-square-o','square-o'),('fa-star','star'),('fa-star-half','star-half'),('fa-stop','stop'),('fa-subscript','subscript'),('fa-tablet','tablet'),('fa-tachometer','tachometer'),('fa-tag','tag'),('fa-tags','tags')
     )

    statistics_icon = models.CharField(max_length=200,choices = ICON_CHOICES)
    statistics_type= models.TextField(max_length=20)
    statistics_count= models.IntegerField()


    class Meta:
        db_table = 'vg_service_statistics'



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    company_name = models.CharField(max_length = 150)
    phone_number = models.CharField(max_length = 20)
    image        = models.ImageField(upload_to = 'media',null=True)
    address      = models.TextField(null=True)

    class Meta:
        db_table = 'vg_user_profile'


class VendorAds(models.Model):
    image = models.ImageField(upload_to = "media")
    title = models.CharField(max_length = 50)
    desc = models.TextField(null=True)

    class Meta:
        db_table = "vg_vendor_ads"
        