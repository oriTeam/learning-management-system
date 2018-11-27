<template>
    <div id="about" class="section bg-white">
        <div class="container">
            <div class="row">
                <div class="col-md-6 animated fadeInRight">
                    <div class="m--margin-bottom-40">
                        <h2>Chào mừng bạn đến với PIEdu</h2>
                        <p class="lead">Hệ thống quản lý môn học tích hợp nhiều tính năng</p>
                    </div>
                    <!-- feature -->
                    <div class="feature">
                        <i class="feature-icon fa fa-flask"></i>
                        <div class="feature-content">
                            <h4>Học online </h4>
                            <p>Giáo trình, tài liệu được upload trực tiếp bởi giảng viên</p>
                        </div>
                    </div>
                    <!-- /feature -->
                    <!-- feature -->
                    <div class="feature">
                        <i class="feature-icon fa fa-users"></i>
                        <div class="feature-content">
                            <h4>Giảng viên có kinh nghiệm</h4>
                            <p>Đội ngũ giảng viên của trường XYZ cóa kinh nghiệm giảng dạy lâu năm</p>
                        </div>
                    </div>
                    <!-- /feature -->
                    <!-- feature -->
                    <div class="feature">
                        <i class="feature-icon fa fa-comments"></i>
                        <div class="feature-content">
                            <h4>Hỗ trợ trao đổi nhóm</h4>
                            <p>Trao đổi, học hỏi từ bạn bè thầy cô thông qua diễn đàn</p>
                        </div>
                    </div>
                    <!-- /feature -->
                </div>
                <div class="col-md-6 animated fadeInLeft">
                    <div class="about-img">
                        <img src="{% static 'images/about.png' %}" alt="">
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'introduce',

    }
</script>
<style>




#about h2 {
    font-size: 30px;
}
#about h4, #about h2 {
    margin-top: 12px;
    margin-bottom: 15px;
    font-weight: 600;
    color: #374050;
}

.lead {
    margin-bottom: 20px;
    font-size: 16px;
    font-weight: 300;
    line-height: 1.4;
}

@media (min-width: 768px) {
    .lead {
        font-size: 21px !important;
    }
}
#about .feature {
    position: relative;
}

.feature + .feature {
    margin-top: 40px;
}

#about .feature .feature-icon {
    position: absolute;
    left: 0;
    top: 0;
    width: 80px;
    height: 80px;
    line-height: 80px;
    text-align: center;
    border-radius: 50%;
    font-size: 30px;
    border: 1px solid #EBEBEB;
    color: #FF6700;
}
.feature-content {
    padding-left: 100px;
}

.about-img > img {
    width: 100%;
}
</style>
