<template>
    <header class="bg-gradient" id="home">
        <div class="section--header m--padding-top-40-desktop">
            <div class="section-shape">
                <img src="../../assets/images/waves-shape.svg" alt="shape image"/>
            </div>
            <div class="container">
                <div class="row">
                    <div class="col-sm-12 col-lg-6 animated bounceInLeft">
                        <div class="intro m--padding-top-50-desktop">
                            <!--<img src="../../static/images/uet.jpg" alt="" width=20% class="m&#45;&#45;img-rounded" style="margin-bottom: 40px">-->
                            <div class="intro_text">
                                <h2 class="intro__title">Hệ thống quản lý môn học</h2>
                                <p class="intro__description">Đại Học Công Nghệ - Đại Học Quốc Gia Hà Nội</p>
                            </div>
                            <div class="intro__buttons my-4">
                                <div class="row">
                                    <div class="col-sm-6">
                                        {% if user.is_authenticated %}

                                        <button class="btn btn-primary" id="test">TEST PLeaSe DONT DELETE</button>

                                        <a href="#"
                                           class="btn m-btn--pill btn-outline-light m-btn--air m-btn--hover-light btn-lg">Khóa
                                            học của tôi</a>

                                        {% else %}
                                        <a href="/login"
                                           class="btn m-btn--pill btn-outline-light m-btn--air m-btn--hover-light btn-lg">Đăng
                                            nhập ngay</a>
                                        {% endif %}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-6 animated fadeInRight hide-sm">
                        <img src="../../assets/images/girl-with-comp.svg" alt="" width="500vw">
                    </div>
                </div>

            </div>
            <div class="shape shape-style-1 shape-primary">
                <span class="circle-150"></span>
                <span class="circle-50"></span>
                <span class="circle-50"></span>
                <span class="circle-75"></span>
                <span class="circle-100"></span>
                <span class="circle-150"></span>
            </div>
        </div>
    </header>
</template>
<script>
    // const IMAGE = "../../assets/images/"
    export default {
        name: 'hero',
        data: function () {
            return {
                // 'waves_shape': '../../../piedu-frontend/static/images/waves-shape.svg',
            }
        }
    }
</script>
<style>
    .bg-gradient {
        background-image: -moz-linear-gradient(135deg, #0098d6 0%, #00cbd6 100%);
        background-image: -webkit-linear-gradient(135deg, #0098d6 0%, #00cbd6 100%);
        background-image: -ms-linear-gradient(135deg, #0098d6 0%, #00cbd6 100%);
        background-image: linear-gradient(135deg, #0098d6 0%, #00cbd6 100%);
    }

    @media (min-width: 992px) {
        .bg-gradient {
            height: 640px;
        }
    }

    .section--header {
        height: 100%;
        position: relative;
        padding-bottom: 5rem;
        /*background: url(../images/.jpg);*/
        /*background: linear-gradient(150deg, #281483 15%, #8f6ed5 70%, #d782d9 94%);*/
        background-position-x: center;
        background-position-y: top;
        background-size: initial;
        background-repeat-x: no-repeat;
        background-repeat-y: no-repeat;
        background-attachment: fixed;
        background-origin: initial;
        background-clip: initial;
        background-color: initial;
        background-attachment: fixed;
    }

    .section-shape {
        bottom: -4px;
        left: 0;
        position: absolute;
        right: 0;

    }

    .section-shape img {
        max-width: 100%;
        min-width: 100%;
        width: 100%;
    }

    .section-circle .shape {
        position: absolute;
        z-index: -1;
        top: 0;
        width: 100%;
        height: 100%;
    }

    .shape-style-1 span {
        width: 120px;
        height: 120px;
        border-radius: 100px 130px 100px 315px;
    }

    .shape span {
        position: absolute;
    }

    .shape-style-1 :nth-child(1) {
        bottom: auto;
        left: -3%;
        top: -20px;
        background: rgba(255, 255, 255, .1);
    }

    .shape-style-1 .circle-150 {
        width: 150px;
        height: 150px;
    }

    .shape-style-1 :nth-child(2) {
        top: 15%;
        right: 10%;
        background: rgba(255, 255, 255, .1);
    }

    .shape-style-1 .circle-50 {
        width: 50px;
        height: 50px;
    }

    .shape-style-1 :nth-child(3) {
        top: 80%;
        right: 40%;
        background: rgba(255, 255, 255, .1);
    }

    .shape-style-1 .circle-75 {
        width: 75px;
        height: 75px;
    }

    .shape-style-1 .circle-100 {
        width: 100px;
        height: 100px;
    }

    .shape-style-1 :nth-child(4) {
        top: 14%;
        right: 47%;
        background: rgba(255, 255, 255, .1);
    }

    .shape-style-1 :nth-child(5) {
        top: 54%;
        right: 60%;
        background: rgba(255, 255, 255, .1);
    }
       .intro {
    display: flex;
    flex-direction: column;
    /*align-items: center;*/
    justify-content: center;
    padding-top: 30px;
}

@media (min-width: 992px) {
    .intro {
        text-align: left;
    }
}

.intro__title {
    padding: 20px 0;
    font-size: 32px !important;
    font-weight: 400;
    font-size: 3rem !important;
}
.intro_text {
    color: #fff;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.11);
    /*text-align: center;*/
}
.intro__description {
    font-size: 18px;
}

</style>
