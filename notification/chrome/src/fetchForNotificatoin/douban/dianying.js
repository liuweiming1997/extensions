import dianyingApi from '../../common/api/douban/dianying';
import storageService from '../../common/chrome_api/storage';
import { popNotice } from '../util';

const ON_SHOW_DIANYING = 'on_show_dianying';
const UP_COMING_DIANYING = 'up_coming_dianying';

class FetchDianYing {
  constructor() {
  }
  init = () => {
    this.fetchOnShowMovie();
    setInterval(() => {
      this.fetchOnShowMovie();
    }, 60000 * 5); // 60s * 5
  }
  fetchOnShowMovie = async () => {
    const result_from_server = await dianyingApi.getOnshowMovie();
    storageService.get({
      [ON_SHOW_DIANYING]: [],
    }, (result) => {
      const result_from_storage = result[[ON_SHOW_DIANYING]];
      const need_to_storage = [];
      for (const idx in result_from_server) {
        let found = false;
        const temp = result_from_server[idx];
        need_to_storage.push({title: temp.title});

        for (const idx_storage in result_from_storage) {
          if (temp.title === result_from_storage[idx_storage].title) {
            found = true;
            break;
          }
        }
        if (!found) {
          popNotice(temp.title, `${temp.region}  ---> ${temp.score}`, temp.img, () => {
            window.open(temp.url);
          });
        }
      }

      // after get
      storageService.set({
        [ON_SHOW_DIANYING]: need_to_storage,
      });

    });
  }
}

const fetchDianYing = new FetchDianYing();
export default fetchDianYing;
