import axios from 'axios';
import router from "./router";
import BACKEND_URL from "./backendServer";

export default {
    send: function (_context, _method, _path, _data, _success, _error) {
        _data.token = _context.$ls.get('token');
        _context.axios({
            method: _method,
            url: BACKEND_URL + _path,
            data: _data,
        }).then((res) => {
            _success(res);
        }).catch((res) => {
            _error(res);
        })
    }
};
