<template>
  <div class="m-portlet w-100">
    <div class="m-portlet__head">
      <div class="m-portlet__head-caption">
        <div class="m-portlet__head-title">
          <h3 class="m-portlet__head-text">
            Tạo lớp học mới
          </h3>
        </div>
      </div>
      <div class="m-portlet__head-tools">
        <ul class="m-portlet__nav">
          <li class="m-portlet__nav-item">
            <a href="#" data-toggle="m-tooltip"
               class="m-portlet__nav-link m-portlet__nav-link--icon"
               data-direction="left" data-width="auto" title=""
               data-original-title="Get help with filling up this form">
              <i class="flaticon-info m--icon-font-size-lg3"></i>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="m-wizard m-wizard--1 m-wizard--success m-wizard--step-first" id="m_wizard">
      <div class="m-portlet__padding-x">
      </div>
      <div class="m-wizard__head m-portlet__padding-x">
        <div class="m-wizard__progress">
          <div class="progress">
            <div class="progress-bar" role="progressbar" aria-valuenow="100"
                 aria-valuemin="0" aria-valuemax="100"
                 style="width: calc(25% + 26px);"></div>
          </div>
        </div>
        <div class="m-wizard__nav">
          <div class="m-wizard__steps">
            <div class="m-wizard__step m-wizard__step--current"
                 m-wizard-target="m_wizard_form_step_1">
              <div class="m-wizard__step-info">
                <a href="#" class="m-wizard__step-number">
                  <span>
                    <span>1</span>
                  </span>
                </a>
                <div class="m-wizard__step-line">
                  <span></span>
                </div>
                <div class="m-wizard__step-label">
                  Thông tin cơ bản
                </div>
              </div>
            </div>
            <div class="m-wizard__step" m-wizard-target="m_wizard_form_step_2">
              <div class="m-wizard__step-info">
                <a href="#" class="m-wizard__step-number">
                  <span>
                    <span>2</span>
                  </span>
                </a>
                <div class="m-wizard__step-line">
                  <span></span>
                </div>
                <div class="m-wizard__step-label">
                  Thời gian của lớp học
                </div>
              </div>
            </div>
            <div class="m-wizard__step" m-wizard-target="m_wizard_form_step_4">
              <div class="m-wizard__step-info">
                <a href="#" class="m-wizard__step-number">
                  <span>
                    <span>3</span>
                  </span>
                </a>
                <div class="m-wizard__step-line">
                  <span></span>
                </div>
                <div class="m-wizard__step-label">
                  Xác nhận tạo lớp học
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="m-wizard__form">
        <form class="m-form m-form--label-align-left m-form--state" id="m_form"
              novalidate="novalidate">
          <div class="m-portlet__body">
            <div class="m-wizard__form-step m-wizard__form-step--current"
                 id="m_wizard_form_step_1">
              <div class="row justify-content-center">
                <div class="col-xl-12">
                  <div class="m-form__section m-form__section--first">
                    <div class="m-form__heading">
                      <h3 class="m-form__heading-title">Thông tin cơ
                        bản</h3>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-xl-2 col-lg-2 col-form-label m--regular-font-size-lg2">
                        Thể loại
                      </label>
                      <div class="col-xl-10 col-lg-10">
                        <select name="country"
                                class="form-control m-input">
                          <option value="">Select</option>
                          <option value="AF">Toán</option>
                          <option value="ZW">CNTT</option>
                        </select>
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-xl-2 col-lg-2 col-form-label m--regular-font-size-lg2">
                        Môn học
                      </label>
                      <div class="col-xl-10 col-lg-10">
                        <select name="country"
                                class="form-control m-input">
                          <option value="">Select</option>
                          <option value="AF">Phát triển Úng dụng Web
                          </option>
                          <option value="ZW">Phát triển Ứng dụng Di
                            Động
                          </option>
                        </select>
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-xl-2 col-lg-2 col-form-label m--regular-font-size-lg2">Tên
                        lớp học</label>
                      <div class="col-xl-10 col-lg-10">
                        <input type="text" name="name"
                               class="form-control m-input"
                               placeholder="">
                        <!--{# <span class="m-form__help">Please enter your first and last names</span>#}-->
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-xl-2 col-lg-2 col-form-label m--regular-font-size-lg2">
                        Mã lớp học</label>
                      <div class="col-xl-10 col-lg-10">
                        <input type="text" name="email"
                               class="form-control m-input"
                               placeholder="">
                        <!--{# <span class="m-form__help">We'll never share your email with anyone else</span>#}-->
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-xl-2 col-lg-2 col-form-label m--regular-font-size-lg2">
                        Mô tả</label>
                      <div class="col-xl-10 col-lg-10">
                                                                        <textarea name="description" id=""
                                                                                  class="form-control m-input w-100"
                                                                                  rows="8"></textarea>
                        <!--{# <span-->
                        <!--class="m-form__help">Enter your valid phone in US phone format. E.g: 1-541-754-3010</span>#}-->
                      </div>
                    </div>
                  </div>
                </div>
              </div>

            </div>

            <!--end: Form Wizard Step 1-->

            <!--begin: Form Wizard Step 2-->
            <div class="m-wizard__form-step" id="m_wizard_form_step_2">
              <div class="row justify-content-center">
                <div class="col-xl-12">
                  <div class="m-form__section m-form__section--first">
                    <div class="m-form__heading">
                      <h3 class="m-form__heading-title">Thời gian</h3>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-form-label col-lg-2 col-sm-12">Ngày
                        bắt đầu</label>
                      <div class="col-lg-10 col-sm-12">
                        <div class="input-group date">
                          <input type="text"
                                 class="form-control m-input"
                                 readonly="" value="09/20/2018"
                                 id="start_datepicker">
                          <div class="input-group-append">
                            <span class="input-group-text">
                              <i class="la la-calendar"></i>
                            </span>
                          </div>
                        </div>
                        <!--{# <span class="m-form__help">Enable clear and today helper buttons</span>#}-->
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-form-label col-lg-2 col-sm-12">Ngày
                        kết thúc</label>
                      <div class="col-lg-10 col-sm-12">
                        <div class="input-group date">
                          <input type="text"
                                 class="form-control m-input"
                                 readonly="" value="05/01/2019"
                                 id="end_datepicker">
                          <div class="input-group-append">
                            <span class="input-group-text">
                              <i class="la la-calendar"></i>
                            </span>
                          </div>
                        </div>
                        <!--{# <span class="m-form__help">Enable clear and today helper buttons</span>#}-->
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-form-label col-lg-2 col-sm-12">Giờ bắt đầu buổi học</label>
                      <div class="col-lg-10 col-md-9 col-sm-12">
                        <input type="text" class="form-control"
                               id="session_start_timepicker" readonly=""
                               placeholder="Select time">
                      </div>
                    </div>
                    <div class="form-group m-form__group row">
                      <label class="col-form-label col-lg-2 col-sm-12">Giờ Kết thúc buổi học</label>
                      <div class="col-lg-10 col-md-9 col-sm-12">
                        <input type="text" class="form-control"
                               id="session_end_timepicker" readonly=""
                               placeholder="Select time">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!--end: Form Wizard Step 2-->
          </div>
          <div class="m-portlet__foot m-portlet__foot--fit m--margin-top-40">
            <div class="m-form__actions m-form__actions">
              <div class="row">
                <div class="col-lg-6 col-sm-12 m--align-left my-2">
                  <button class="btn btn-secondary m-btn m-btn--custom m-btn--icon"
                          data-wizard-action="prev">
                    <span>
                      <i class="la la-arrow-left"></i>&nbsp;&nbsp;
                      <span>Quay lại</span>
                    </span>
                  </button>
                </div>
                <div class="col-lg-6 col-sm-12 m--align-right my-2">
                  <button class="btn btn-primary m-btn m-btn--custom m-btn--icon"
                          data-wizard-action="submit">
                    <span>
                      <i class="la la-check"></i>&nbsp;&nbsp;
                      <span>Tạo lớp học</span>
                    </span>
                  </button>
                  <button class="btn btn-success m-btn m-btn--custom m-btn--icon"
                          data-wizard-action="next">
                    <span>
                      <span>Tiếp tục</span>&nbsp;&nbsp;
                      <i class="la la-arrow-right"></i>
                    </span>
                  </button>
                </div>
                <div class="col-lg-2"></div>
              </div>
            </div>
          </div>

          <!--end: Form Actions -->
        </form>
      </div>

      <!--end: Form Wizard Form-->
    </div>

    <!--end: Form Wizard-->
  </div>
</template>
