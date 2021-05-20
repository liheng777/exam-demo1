import Axios from 'axios/index'

const base = process.env.NODE_ENV === 'development' ? '/' : window.baseUrl

const instance = Axios.create({
  validateStatus: status => status >= 200 && status < 300,
  withCredentials: true,
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  baseURL: base
})

export default instance
