<template>
    <div class="section" id="gallery">
        <div class="container">
            <div class="section-title">
                <h3>Các Khóa học</h3>
            </div>
            <div class="img-gallery owl-carousel owl-theme">
                <!--{% for i in categories %}-->
                <div class="w-100">
                    <div class="category-icon-title text-center ">
                        <div class="category-icon">
                            <i class="text-gradiant fa fa-calculator"></i>
                        </div>
                        <div class="category-title">
                            <!--<h4>{{ i.name }}</h4>-->
                        </div>
                    </div>
                </div>
                <!--{% endfor %}-->
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'coursecategory',
    }
</script>
<style>

.category-icon-title {
    background-color: #f6fafb;
    padding: 35px;
    border-radius: 4px;
    -webkit-transition: .3s all ease-in-out;
    -o-transition: .3s all ease-in-out;
    transition: .3s all ease-in-out;
    position: relative;
    height: 90%;
}
.category-icon {
    position: relative;
    z-index: 1;
}

.category-icon-title:hover {
    -webkit-box-shadow: 0px 10px 15px 2px rgba(0, 0, 0, 0.1);
    box-shadow: 0px 10px 15px 2px rgba(0, 0, 0, 0.1);
}

.category-icon-title:hover .category-icon i {
    color: #fff;
    -webkit-text-fill-color: inherit;
}
.category-icon i {
    font-size: 60px;
}
.text-gradiant {
    background: -moz-linear-gradient(left, #01a6fd 0%, #17d0cf 100%);
    background: -webkit-gradient(left top, right top, color-stop(0%, #01a6fd), color-stop(100%, #17d0cf));
    background: -webkit-linear-gradient(left, #01a6fd 0%, #17d0cf 100%);
    background: -o-linear-gradient(left, #01a6fd 0%, #17d0cf 100%);
    background: -ms-linear-gradient(left, #01a6fd 0%, #17d0cf 100%);
    background-clip: text;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.category-title {
    margin-top: 10px;
    position: relative;
    z-index: 1;
}

.category-icon-title:hover .category-title h4 {
    color: #fff;
}
.category-title h4 {
    font-size: 18px;
    font-weight: 500;
    color: #333333;
}

.category-icon-title:hover::after {
    opacity: 1;
    -webkit-transform: scale(1);
    -ms-transform: scale(1);
    transform: scale(1);
}
.category-icon-title:after {
    position: absolute;
    width: 100%;
    height: 100%;
    content: '';
    background: #17d0cf;
    background: -moz-linear-gradient(left, #01a6fd 0%, #17d0cf 51%, #01a6fd 100%);
    background: -webkit-gradient(left top, right top, color-stop(0%, #4eb3bf), color-stop(51%, #17d0cf), color-stop(100%, #4eb3bf));
    background: -webkit-linear-gradient(left, #01a6fd 0%, #17d0cf 51%, #0071b0 100%);
    background: -o-linear-gradient(left, #01a6fd 0%, #17d0cf 51%, #01a6fd 100%);
    background: -ms-linear-gradient(left, #01a6fd 0%, #17d0cf 51%, #01a6fd 100%);
    background: -webkit-gradient(linear, left top, right top, from(#01a6fd), color-stop(51%, #17d0cf), to(#01a6fd));
    background: -webkit-linear-gradient(left, #01a6fd 0%, #17d0cf 51%, #01a6fd 100%);
    background: linear-gradient(to right, #01a6fd 0%, #17d0cf 51%, #01a6fd 100%);
    background-size: 200% auto;
    -webkit-transition: .3s all ease-in-out;
    -o-transition: .3s all ease-in-out;
    transition: .3s all ease-in-out;
    left: 0;
    top: 0;
    z-index: 0;
    opacity: 0;
    border-radius: 4px;
    -webkit-transform: scale(0);
    -ms-transform: scale(0);
    transform: scale(0);
}
</style>
