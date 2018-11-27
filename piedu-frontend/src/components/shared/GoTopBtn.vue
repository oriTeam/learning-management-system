<template>
    <div>
        <button class="btn btn-lg btn-info animated bounceInUp" data-toggle="tooltip" data-placement="left" id="gotop"
                title="Lên trên cùng">
            <i class="fa fa-angle-double-up m--regular-font-size-lg4"></i>
        </button>
    </div>
</template>
<script>
    export default {
        name: 'go-top',
        mounted() {
            window.onscroll = function () {
                if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                    $("#gotop").css({display: "block"});
                }
                else $("#gotop").css({display: "none"});
            };

            $("#gotop").click(function () {
                $("html, body").animate({
                    scrollTop: $("body").offset().top
                    // document.documentElement.scrollTop = 0,
                }, 250);
            });
        }
    }
</script>
<style>
    #gotop {
        float: right;
        position: fixed;
        bottom: 25px;
        right: 30px;
        display: none;
        z-index: 8;
        transition: 0.3s;
        border-radius: 50%;
    }
</style>
