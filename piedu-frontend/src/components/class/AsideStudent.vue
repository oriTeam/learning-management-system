<template>
        <div>
        <button class="m-aside-left-close  m-aside-left-close--skin-light " id="m_aside_left_close_btn"><i
                class="la la-close"></i></button>
        <div id="m_aside_left" class="m-grid__item	m-aside-left  m-aside-left--skin-light h-100">
            <!-- BEGIN: Aside Menu -->
            <div id="m_ver_menu"
                 class="m-aside-menu  m-aside-menu--skin-light m-aside-menu--submenu-skin-light "
                 m-menu-vertical="1" m-menu-scrollable="0" m-menu-dropdown-timeout="500">
                <ul class="m-menu__nav  m-menu__nav--dropdown-submenu-arrow ">
                    <li class="m-menu__section m-menu__section--first">
                        <h4 class="m-menu__section-text m--regular-font-size-lg2">Lọc môn học</h4>
                        <i class="m-menu__section-icon flaticon-more-v3"></i>
                    </li>
                    <li class="m-menu__item m-menu__item--submenu" aria-haspopup="true"
                        m-menu-submenu-toggle="hover"><a href="javascript:;"
                                                         class="m-menu__link m-menu__toggle"><i
                            class="m-menu__link-icon flaticon-layers"></i><span
                            class="m-menu__link-text">Theo chủ đề</span><i
                            class="m-menu__ver-arrow la la-angle-right"></i></a>
                        <div class="m-menu__submenu "><span class="m-menu__arrow"></span>
                            <ul class="m-menu__subnav">
                                <li class="m-menu__item  m-menu__item--parent" aria-haspopup="true"><span
                                        class="m-menu__link"><span
                                        class="m-menu__link-text">Resources</span></span>
                                </li>
                                <li class="m-menu__item " aria-haspopup="true"><a href="inner.html"
                                                                                  class="m-menu__link "><i
                                        class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                        class="m-menu__link-text">Toán</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html" class="m-menu__link "><i
                                        class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                        class="m-menu__link-text">Công nghệ thông tin</span></a></li>
                                <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1"><a
                                        href="inner.html" class="m-menu__link "><i
                                        class="m-menu__link-bullet m-menu__link-bullet--dot"><span></span></i><span
                                        class="m-menu__link-text">Ngoại Ngữ</span></a></li>
                            </ul>
                        </div>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        mounted() {
            let el = document.getElementById('m_aside_left');
            let rect = el.getBoundingClientRect();
            let fixmeTop = rect.top + document.body.scrollTop;
            window.addEventListener('scroll', function () {
                let currentScroll = window.scrollY + 65;
                let el = document.getElementById('m_aside_left');
                if (currentScroll >= fixmeTop && Math.max(document.documentElement.clientWidth, window.innerWidth || 0) >= 1025) {
                    if (el.classList)
                        el.classList.add('fixed-aside');
                    else
                        el.className += ' ' + 'fixed-aside';
                } else {
                    if (el.classList)
                        el.classList.remove('fixed-aside');
                    else
                        el.className = el.className.replace(new RegExp('(^|\\b)' + 'fixed-aside'.split(' ').join('|') + '(\\b|$)', 'gi'), ' ');
                }
            });
        },
        methods: {}

    }
</script>
<style lang="scss">
    .fixed-aside {
        position: fixed;
        top: 65px;
        left: 0;
    }

    #m_aside_left {
        width: 23.5rem;
    }

    @media (max-width: 1280px) {
        .m-aside-left {
            display: block !important;
            z-index: 1001;
            position: fixed;
            -webkit-overflow-scrolling: touch;
            top: 0;
            bottom: 0;
            overflow-y: auto;
            -webkit-transform: translate3d(0, 0, 0);
            backface-visibility: hidden;
            -webkit-backface-visibility: hidden;
            width: 275px !important;
            -webkit-transition: all .3s ease;
            transition: all .3s ease;
            left: -285px;
        }
    }

    @media (max-width: 1200px) {
        #m_aside_left {
            z-index: 1031;
        }

        .m-aside-left.m-aside-left--on {
            -webkit-transition: all .3s ease;
            transition: all .3s ease;
            left: 0;
        }

        #m_aside_left_close_btn {
            z-index: 1032;
        }

        .m-aside-left-close.m-aside-left-close--skin-light {
            background-color: #eeeef5;
        }

        .m-aside-left-close {
            left: -25px;
            width: 25px;
            height: 25px;
            top: 1px;
            z-index: 1002;
            -webkit-transition: all .3s ease;
            transition: all .3s ease;
            position: fixed;
            border: 0;
            -webkit-box-shadow: none;
            box-shadow: none;
            border-radius: 3px;
            cursor: pointer;
            outline: 0 !important;
            text-align: center;
            vertical-align: center;
            display: inline-block;
        }

        .m-aside-left--on .m-aside-left-close {
            -webkit-transition: all .3s ease;
            transition: all .3s ease;
            left: 249px;
        }
    }
</style>
