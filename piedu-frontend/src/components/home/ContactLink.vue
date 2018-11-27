<template>
    <div class="section">
        <div class="container">
            <div class="row">
                <div class="col-md-6 px-5">
                    <img src="{% static 'images/envelope.svg' %}" alt="dual phone" class="img-fluid">
                </div>
                <div class="col-md-6 d-flex align-items-center">
                    <div>
                        <h2>Bạn có phản hồi, thắc mắc khác ?</h2>
                        <p class="mb-4">Chúng tôi luôn sẵn sàng lắng nghe mọi ý kiến đóng góp của các bạn. Điều này giúp
                            chúng tôi cải thiện hệ thống để đem lại trải nghiệm tốt hơn cho cả Giảng viên và các sinh
                            viên </p>
                        <a href="/contact" class="btn btn-primary">Liên hệ</a></div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        name: 'contactlink',

    }
</script>
