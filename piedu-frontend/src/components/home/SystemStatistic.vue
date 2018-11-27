<template>
    <div class="section light-bg" id="features">
        <div class="container">
            <div class="section-title">
                <h3>Thống kê hệ thống</h3>
            </div>
            <div class="row">
                <div class="col-12 col-lg-4">
                    <div class="card features">
                        <div class="card-body">
                            <div class="media">
                                <span class="fa fa-user-graduate gradient-fill statistic-icon mx-3"></span>
                                <div class="media-body">
                                    <h4 class="card-title">
                                        <span class="count">70</span>
                                        <span><span class="fa fa-plus pb-2 vertical-align-top mt-2"></span><span
                                                class="fa fa-plus pb-2 vertical-align-top mt-2"></span></span>
                                        <span class="statistic-text"> giảng viên</span>
                                    </h4>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12 col-lg-4">
                    <div class="card features">
                        <div class="card-body">
                            <div class="media">
                                <span class="fa fa-users gradient-fill statistic-icon mx-3"></span>
                                <div class="media-body">
                                    <h4 class="card-title">
                                        <span class="count">1000</span>
                                        <span><span class="fa fa-plus pb-2 vertical-align-top mt-2"></span><span
                                                class="fa fa-plus pb-2 vertical-align-top mt-2"></span></span>
                                        <span class="statistic-text"> sinh viên</span>
                                    </h4>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12 col-lg-4">
                    <div class="card features">
                        <div class="card-body">
                            <div class="media">
                                <span class="fa fa-file-alt gradient-fill statistic-icon mx-3"></span>
                                <div class="media-body">
                                    <h4 class="card-title">
                                        <span class="count">200</span>
                                        <span><span class="fa fa-plus pb-2 vertical-align-top mt-2"></span><span
                                                class="fa fa-plus pb-2 vertical-align-top mt-2"></span></span>
                                        <span class="statistic-text"> tài liệu</span>
                                    </h4>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'systemstatistic',
    }
</script>
<style>

.gradient-fill:before {
    color: #fc73b4;
    background: -moz-linear-gradient(top, #1ba6de 0%, #a4d6e7 100%);
    background: -webkit-linear-gradient(top, #1ba6de 0%, #a4d6e7 100%);
    background: linear-gradient(to bottom, #1ba6de 0%, #a4d6e7 100%);
    -webkit-background-clip: text;
    /*background-clip: text;*/
    -webkit-text-fill-color: transparent;
}

.card.features {
    border: 0;
    border-radius: 3px;
    box-shadow: 0px 5px 7px 0px rgba(0, 0, 0, 0.04);
    transition: all 0.3s ease;
}

@media (max-width:991px) {
    .card.features {
        margin-bottom: 2rem;
    }
    [class^="col-"]:last-child .card.features {
        margin-bottom: 0;
    }
}

.card.features:before {
    content: "";
    position: absolute;
    width: 3px;
    color: #fc73b4;
    background: -moz-linear-gradient(top, #1ba6de 0%, #a4d6e7 100%);
    background: -webkit-linear-gradient(top, #1ba6de 0%, #a4d6e7 100%);
    background: linear-gradient(to bottom, #1ba6de 0%, #a4d6e7 100%);
    top: 0;
    bottom: 0;
    left: 0;
}

.card-title {
    font-size: 2.5rem;
}
.vertical-align-top {
    vertical-align: top;
}
.statistic-icon {
    font-size: 4rem;
}
.statistic-text {
    font-size: 1.75rem;
    font-weight: lighter;
}

.card.features:hover {
    transform: translateY(-3px);
    -moz-box-shadow: 0px 5px 30px 0px rgba(0, 0, 0, 0.08);
    -webkit-box-shadow: 0px 5px 30px 0px rgba(0, 0, 0, 0.08);
    box-shadow: 0px 5px 30px 0px rgba(0, 0, 0, 0.08);
}
</style>
