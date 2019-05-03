/*global chrome*/
class StorageService {
  constructor() {
  }

  get = (object, callback=null) => {
    chrome.storage.sync.get(object, (result) => {
      if (callback) {
        callback(result);
      }
    });
  }

  set = (object) => {
    chrome.storage.sync.set(object, () => {
      console.log(`save sync success ${JSON.stringify(object)}`);
    });
  }
}

const storageService = new StorageService();
export default storageService;
