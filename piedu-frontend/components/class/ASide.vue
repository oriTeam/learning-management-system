<template>
  <div>
    <button class="m-aside-left-close  m-aside-left-close--skin-light " id="m_aside_left_close_btn"><i
      class="la la-close"></i></button>
    <div id="m_aside_left" class="m-grid__item	m-aside-left  m-aside-left--skin-light w-100 h-100">
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
