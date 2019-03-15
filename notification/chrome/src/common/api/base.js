import log from '../lib/log';

const OPT = Object.freeze({
  method: 'GET',
  mode: 'cors',
  redirect: 'follow',
  credentials: 'include',
  headers: new Headers({
    'Content-Type': 'text/plain',
  })
});

const processResponse = async (response) => {
  const contentType = response.headers.get('Content-Type');
  if (!contentType) {
    throw "no content type";
  } else {
    if(contentType.indexOf('text') !== -1) {
      return await response.text()
    } else if(contentType.indexOf('form') !== -1) {
      return await response.formData();
    } else if(contentType.indexOf('video') !== -1) {
      return await response.blob();
    } else if(contentType.indexOf('json') !== -1) {
      return await response.json();
    }
  }
}

const processOptions = (options) => {
  return Object.assign(options, OPT);
}

export default class RequestBase {
  constructor() {
  }

  doRequest = async (url, options) => {
    try {
      const response = await fetch(url, options);
      if (response.status !== 200) {
        throw response;
      } else {
        return await processResponse(response)
      }
    } catch(fetchError) {
      console.log(fetchError);
      const error = new Error(fetchError.statusText);
      error.data = fetchError;
      // TODO:(weimingliu) add hint messgae for error
      // throw error;
    }
  }

  get = async (url, options = {}) => {
    const fetchOptions = processOptions(options);
    fetchOptions.method = 'GET';
    return await this.doRequest(url, fetchOptions);
  }
  post = () => {}
  put = () => {}
  del = () => {}
  options = () => {}
};
