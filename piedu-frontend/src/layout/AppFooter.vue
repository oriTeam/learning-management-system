<template>
    <div>
        <div id="contact-cta" class="section">
            <div class="bg-image bg-parallax overlay"></div>
            <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-8 text-center">
                        <h2 class="white-text">Đăng ký nhận Email thông báo </h2>
                        <p class="lead white-text">Mỗi khi có khóa học mới, chúng tôi sẽ email thông báo đến bạn</p>
                        <a class="main-button icon-button" href="#">Đăng ký ngay</a>
                    </div>
                </div>
            </div>
        </div>
        <footer id="footer" class="section">
            <div class="container">
                <div class="row">
                    <div class="col-md-5">
                        <div class="footer-logo">
                            <a class="navbar-brand" href="index.html">
                                <strong style="font-size: 30px">
                                    <i class="fa fa-chalkboard" style="font-size: 30px"></i> PIEdu</strong>
                            </a>
                        </div>
                    </div>
                    <div class="col-md-7">
                        <ul class="footer-nav">
                            <li><router-link to="/">TRANG CHỦ</router-link></li>
                            <li><router-link to="/course/my">KHÓA HỌC CỦA TÔI</router-link></li>
                            <li><router-link to="/course/all">TẤT CẢ KHÓA HỌC</router-link></li>
                            <li><router-link to="/contact">LIÊN HỆ</router-link></li>
                            <li><router-link to="/help">TRỢ GIÚP</router-link></li>
                        </ul>
                    </div>
                </div>
                <div id="bottom-footer" class="row">
                    <div class="col-md-7">
                        <div class="footer-copyright">
                            <span>© Copyright 2018. All Rights Reserved. | Team PIEdu - UET -VNU <i class="fa fa-heart"
                                                                                      aria-hidden="true"></i></span>
                        </div>
                    </div>
                    <div class="col-md-5">
                        <ul class="footer-social">
                            <li><a href="#" class="facebook"><i class="fab fa-facebook-f"></i></a></li>
                            <li><a href="#" class="twitter"><i class="fab fa-twitter"></i></a></li>
                            <li><a href="#" class="google-plus"><i class="fab fa-google-plus-g"></i></a></li>
                            <li><a href="#" class="instagram"><i class="fab fa-instagram"></i></a></li>
                            <li><a href="#" class="youtube"><i class="fab fa-youtube"></i></a></li>
                            <li><a href="#" class="linkedin"><i class="fab fa-linkedin"></i></a></li>
                        </ul>
                    </div>
                </div>
                <!-- row -->
            </div>
            <!-- /container -->
        </footer>
    </div>
</template>
<script>
    export default {
        name: "Footer",
    }
</script>
<style>
    .bg-image.bg-parallax {
        background-attachment: fixed;
    }

    .bg-image {
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        background-position: center;
        background-size: cover;
    }

    .bg-image.overlay:after {
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        top: 0;
        bottom: 0;
        background-image: -webkit-gradient(linear, left top, left bottom, from(#374050), to(#798696));
        background-image: linear-gradient(to bottom, #374050 0%, #798696 100%);
        opacity: 0.7;
    }

    .white-text {
        color: #FFF;
    }

    #contact-cta h2 {
        margin-top: 12px;
        margin-bottom: 15px;
        font-weight: 600;
        /*color: #374050;*/
    }

    #contact-cta > .bg-image {
        background: url("../../public/img/cta2-background.jpg") !important;
    }


    .main-button {
        position: relative;
        /* display: inline-block; */
        padding: 10px 30px;
        background-color: #FF6700;
        border: 2px solid transparent;
        border-radius: 40px;
        color: #FFF;
        -webkit-transition: 0.2s all;
        transition: 0.2s all;
    }

    .main-button.icon-button:after {
        content: "\f178";
        font-family: FontAwesome;
        position: absolute;
        width: 30px;
        right: 15px;
        text-align: center;
        opacity: 0;
        -webkit-transition: 0.2s all;
        transition: 0.2s all;
    }

    .main-button.icon-button:hover, .main-button.icon-button:focus {
        padding-right: 45px;
        padding-left: 45px;
    }

    .main-button:hover, .main-button:focus {
        background-color: #fff;
        border: 2px solid #FF6700;
        color: #FF6700;
    }

    #contact-cta a:hover, #contact-cta a:focus {
        text-decoration: none;
        outline: none;
        color: #374050;
        opacity: 0.9;
    }

    #footer {
        background-color: #fff;
    }

    .footer-nav {
        text-align: right;
        padding: 20px 0px;
    }

    ul, ol {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    .footer-nav li {
        display: inline-block;
        margin-left: 15px;
    }

    .footer-nav li a {
        text-decoration: none;
        display: block;
        text-transform: uppercase;
        -webkit-transition: 0.2s color;
        transition: 0.2s color;
        font-weight: bold;
    }

    .footer-nav li a:hover, .footer-nav li a:focus {
        color: #FF6700;
    }

    .footer-nav li a:hover:after, .footer-nav li a:focus:after {
        -webkit-transform: translateY(0px);
        -ms-transform: translateY(0px);
        transform: translateY(0px);
        opacity: 1;
    }

    .footer-nav li a:after {
        content: "";
        display: block;
        height: 2px;
        background-color: #FF6700;
        width: 100%;
        -webkit-transform: translateY(5px);
        -ms-transform: translateY(5px);
        transform: translateY(5px);
        opacity: 0;
        -webkit-transition: 0.2s all;
        transition: 0.2s all;
    }

    #bottom-footer {
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #EBEBEB;
    }

    .footer-social {
        text-align: right;
    }

    .footer-social li {
        display: inline-block;
        margin-left: 10px;
    }

    .footer-social li a {
        display: block;
        width: 40px;
        height: 40px;
        line-height: 40px;
        text-align: center;
        border-radius: 50%;
        color: #FFF;
        background-color: #EBEBEB;
        -webkit-transition: 0.2s opacity;
        transition: 0.2s opacity;
    }

    .footer-social li a.facebook {
        background-color: #3b5998;
    }

    .footer-social li a.twitter {
        background-color: #55acee;
    }

    .footer-social li a.google-plus {
        background-color: #dd4b39;
    }

    .footer-social li a.instagram {
        background-color: #e95950;
    }

    .footer-social li a.youtube {
        background-color: #ff0000;
    }

    .footer-social li a.linkedin {
        background-color: #007bb5;
    }

    .footer-copyright {
        line-height: 40px;
    }

    @media (max-width: 991px) {
        .footer-logo {
            text-align: center;
        }

        .footer-nav {
            text-align: center;
        }

        .footer-nav li {
            margin-top: 10px;
        }

        .footer-social {
            text-align: center;
        }

        .footer-social li {
            margin-top: 10px;
        }

        .footer-copyright {
            text-align: center;
            line-height: inherit;
            margin-top: 20px;
        }
    }
</style>
