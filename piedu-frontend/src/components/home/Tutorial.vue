<template>
    <div class="section">
        <div class="container">
            <div class="row mb-4 justify-content-center">
                <div class="section-header text-center">
                    <h2>Bắt đầu với hệ thống ...</h2>
                </div>
            </div>
            <div class="row">
                <div class="col-md-7 d-flex align-items-center">
                    <ul class="list-unstyled ui-steps">
                        <li class="media">
                            <div class="circle-icon mr-4">1</div>
                            <div class="media-body">
                                <h5>Đăng nhập bằng tài khoản sinh viên/ giảng viên</h5>
                                <p class="mb-0">Tài khoản và mật khẩu mặc định là mã sinh viên/ mã giảng viên</p>
                                <a href="/login" class="m--regular  -font-size-lg1"> <i
                                        class="fa fa-angle-double-right"></i> &nbsp;<em>Đăng nhập ngay</em> </a>
                            </div>
                        </li>
                        <li class="media my-4">
                            <div class="circle-icon mr-4">2</div>
                            <div class="media-body">
                                <h5>Thay đổi thông tin tài khoản</h5>
                                <p>Bao gồm việc thay đổi mật khẩu và các thông tin cá nhân như email, số điện thoại, ảnh
                                    đại diện, ... </p>
                            </div>
                        </li>
                        <li class="media">
                            <div class="circle-icon mr-4">3</div>
                            <div class="media-body">
                                <h5>Khám phá hệ thống</h5>
                                <p>Khám phá và tham gia các khóa học đói với sinh viên <br> Tạo mới các khóa học và chấp
                                    nhận yêu cầu tham gia của sinh viên đối với giảng viên </p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div class="col-md-5 py-lg-5">
                    <img src="{% static 'images/study.svg' %}" alt="iphone" class="img-fluid mt-lg-5">
                </div>

            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'tutorial',
    }
</script>
<style>
    .circle-icon {
    box-shadow: 0px 9px 32px 0px rgba(0, 0, 0, 0.07);
    padding: 10px;
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-bottom: 1.5rem;
    background-color: #FFF;
    color: #f4683b;
    font-size: 48px;
    text-align: center;
    line-height: 80px;
    font-weight: 300;
    transition: all 0.3s ease;
}

@media (max-width:992px) {
    .circle-icon {
        width: 70px;
        height: 70px;
        font-size: 28px;
        line-height: 50px;
    }
}

.ui-steps li:hover .circle-icon {
    background-image: -moz-linear-gradient( 122deg, #1ba6de 0%, #a4d6e7 100%);
    background-image: -webkit-linear-gradient( 122deg, #1ba6de 0%, #a4d6e7 100%);
    background-image: -ms-linear-gradient( 122deg, #1ba6de 0%, #a4d6e7 100%);
    background-image: linear-gradient( 122deg, #1ba6de 0%, #a4d6e7 100%);
    box-shadow: 0px 9px 32px 0px rgba(0, 0, 0, 0.09);
    color: #FFF;
}

.ui-steps li {
    padding: 15px 0;
}

.ui-steps li:not(:last-child) {
    border-bottom: 1px solid #9ed4e6;
}
</style>
