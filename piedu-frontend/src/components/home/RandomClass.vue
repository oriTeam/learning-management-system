<template>
    <div id="courses" class="section light-bg">
        <div class="container">
            <div class="row justify-content-center">
                <div class="section-header text-center">
                    <h2>Khám phá lớp học</h2>
                    <p class="lead">Các môn học bắt buộc, bổ trợ, chuyên ngành, ...</p>
                </div>
            </div>
            <div id="courses-wrapper">
                <div class="row">
                    {% for i in '1234' %}
                        <div class="col-md-3 col-sm-6 col-xs-6">
                            <div class="course">
                                <a href="#" class="course-img">
                                    <img src="{% static 'images/code.jpg' %}" alt="">
                                    <i class="course-link-icon fa fa-link"></i>
                                </a>
                                <a class="course-title" href="#">Nhập môn an toàn thông tin</a>
                                <div class="course-details">
                                    <span class="course-category">CNTT</span>
                                    <span class="course-price course-free">TS. Nguyễn Đại Thọ</span>
                                </div>
                            </div>
                        </div>
                    {% endfor %}
                </div>
            </div>
            <div class="row justify-content-center m--margin-top-30">
                <div class="center-btn">
                    <a class="main-button icon-button" href="#">Xem thêm lớp học ...</a>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'randomclass',

    }
</script>
<style>

.course {
	margin-top:20px;
	margin-bottom:20px;
}

.course .course-img {
	position: relative;
	display:block;
	margin-bottom:20px;
	border-radius:4px;
	overflow:hidden;
}

.course .course-img > img {
	width:100%;
}

.course-img:after {
	content:"";
	position:absolute;
	left:0;
	right:0;
	bottom:0;
	top:0;
	background-color:#9ad2e66b;
	opacity:0;
	-webkit-transition:0.2s opacity;
	transition:0.2s opacity;
}

.course .course-img:hover:after {
	opacity:0.7;
}

.course .course-img .course-link-icon {
	position:absolute;
	left:50%;
	top:50%;
	-webkit-transform: translate(-50% , calc(-50% - 15px));
	    -ms-transform: translate(-50% , calc(-50% - 15px));
	        transform: translate(-50% , calc(-50% - 15px));
	width:40px;
	height:40px;
	line-height:40px;
	text-align:center;
	border:2px solid #fff;
	color:#fff;
	border-radius:50%;
	opacity:0;
	z-index:10;
	-webkit-transition:0.2s all;
	transition:0.2s all;
}

.course .course-img:hover .course-link-icon {
	-webkit-transform: translate(-50% , -50%);
	    -ms-transform: translate(-50% , -50%);
	        transform: translate(-50% , -50%);
	opacity:1;
}

.course .course-title {
	display:block;
	height:42px;
}

.course .course-details {
	margin-top: 20px;
	padding-top: 10px;
	border-top: 1px solid #EBEBEB;
}

.course .course-details .course-price {
	float: right;
}

.course .course-details .course-price.course-free {
	color: green;
}

.course .course-details .course-price.course-premium {
	color: #FF6700;
}

#courses .center-btn {
	text-align:center;
	margin-top:40px;
}

</style>
