
Vue.component('profile-nabar',{
    data: function () {
        return {
          count: 0
        }
      },
    template : `<div><div class="m-card-profile">
    <div class="m-card-profile__title m--hide">
        Your Profile
    </div>
    <div class="m-card-profile__pic">
        <div class="m-card-profile__pic-wrapper">
            <img src="Uploads/39007042_2193527620973537_111659395825270784_n.jpg" alt="">
        </div>
    </div>
    <div class="m-card-profile__details">
        <span class="m-card-profile__name">Mark Andre</span>
        <a href="" class="m-card-profile__email m-link">mark.andre@gmail.com</a>
    </div>
</div>
<!-- BEGIN: Aside Menu -->

<div id="m_ver_menu" class="m-aside-menu  m-aside-menu--skin-light m-aside-menu--submenu-skin-light " m-menu-vertical="1"
    m-menu-scrollable="0" m-menu-dropdown-timeout="500">
    
    <ul class="m-menu__nav  m-menu__nav--dropdown-submenu-arrow ">
        <li class="m-menu__section m-menu__section--first">
            <h4 class="m-menu__section-text">My profile</h4>
            <i class="m-menu__section-icon flaticon-more-v3"></i>
        </li>
        <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1">
            <a href="#" class="m-menu__link ">
                <i class="m-menu__link-icon flaticon-suitcase"></i>
                <span class="m-menu__link-text">Thông tin cá nhân </span>
            </a>
        </li>
        <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1">
            <a href="#" class="m-menu__link ">
                <i class="m-menu__link-icon flaticon-suitcase"></i>
                <span class="m-menu__link-text">Đổi mật khẩu </span>
            </a>
        </li>

        <li class="m-menu__section ">
            <h4 class="m-menu__section-text">My courses</h4>
            <i class="m-menu__section-icon flaticon-more-v3"></i>
        </li>

        <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1">
            <a href="#" class="m-menu__link ">
                <i class="m-menu__link-icon flaticon-alert"></i>
                <span class="m-menu__link-title">
                    <span class="m-menu__link-wrap">
                        <span class="m-menu__link-text">Đang diễn ra</span>
                        <span class="m-menu__link-badge">
                            <span class="m-badge m-badge--danger">6</span>
                        </span>
                    </span>
                </span>
            </a>
        </li>

        <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1">
            <a href="#" class="m-menu__link ">
                <i class="m-menu__link-icon flaticon-alert"></i>
                <span class="m-menu__link-title">
                    <span class="m-menu__link-wrap">
                        <span class="m-menu__link-text">Đã hoàn thành</span>
                        <span class="m-menu__link-badge">
                            <span class="m-badge m-badge--danger">34</span>
                        </span>
                    </span>
                </span>
            </a>
        </li>



        <li class="m-menu__section ">
            <h4 class="m-menu__section-text">Tùy chọn khác</h4>
            <i class="m-menu__section-icon flaticon-more-v3"></i>
        </li>
        <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1">
            <a href="#" class="m-menu__link ">
                <i class="m-menu__link-icon flaticon-suitcase"></i>
                <span class="m-menu__link-text">Liên hệ quản trị viên </span>
            </a>
        </li>

        <li class="m-menu__item " aria-haspopup="true" m-menu-link-redirect="1">
            <a href="#" class="m-menu__link ">
                <i class="m-menu__link-icon flaticon-settings"></i>
                <span class="m-menu__link-text">About</span>
            </a>
        </li>
    </ul>
</div></div>`
});
new Vue({ el: '#m_aside_left', });
