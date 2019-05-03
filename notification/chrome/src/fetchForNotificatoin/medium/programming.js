import programmingApi from '../../common/api/medium/programming';
import storageService from '../../common/chrome_api/storage';
import { popNotice } from '../util';
import ox from './icons8-year-of-ox-64.png';

const PROGRAMMING_KEY = 'programming_key';

class FetchProgramming {
  constructor() {}

  init = () => {
    this.fetch();
    setInterval(() => {
      this.fetch();
    }, 60000 * 5);
  }

  fetch = async () => {
    const result_from_server = await programmingApi.getAllProgrammingBlog();
    const need_to_storage = {};

    storageService.get({
      [PROGRAMMING_KEY]: {},
    }, (result) => {
      const result_from_storage = result[PROGRAMMING_KEY];
      for (const idx_from_server in result_from_server) {
        const temp = result_from_server[idx_from_server];
        need_to_storage[temp.title] = true;
        if (result_from_storage[temp.title]) {
          continue;
        }

        popNotice('new blog', temp.title, ox, () => {
          window.open(temp.url);
        });
      }
      storageService.set({
        [PROGRAMMING_KEY]: need_to_storage,
      });
    });
  }
}

const fetchProgramming = new FetchProgramming();
export default fetchProgramming;
