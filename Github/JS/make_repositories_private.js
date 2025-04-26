const axios = require('axios');

const GITHUB_USERNAME = '';
const GITHUB_TOKEN = '';      

async function makeReposPrivate() {
  try {
    const reposResponse = await axios.get(`https://api.github.com/user/repos?per_page=100`, {
      headers: {
        Authorization: `token ${GITHUB_TOKEN}`
      }
    });

    const repos = reposResponse.data;

    for (const repo of repos) {
      if (!repo.private) { 
        console.log(`Making it private: ${repo.name}...`);

        try {
          await axios.patch(`https://api.github.com/repos/${GITHUB_USERNAME}/${repo.name}`, {
            private: true
          }, {
            headers: {
              Authorization: `token ${GITHUB_TOKEN}`
            }
          });

          console.log(`✅ ${repo.name} is now private.`);
        } catch (patchError) {
          console.error(`❌ Failed to make ${repo.name} private:`, patchError.response?.data || patchError.message);
          console.log('➡️ Skipping to Next Repository.');
        }

      } else {
        console.log(`⚡ ${repo.name} is already private, skipping.`);
      }
    }

    console.log('🏁 All repos have been processed.');
  } catch (error) {
    console.error('❌ Failed to search repos:', error.response?.data || error.message);
  }
}

makeReposPrivate();
