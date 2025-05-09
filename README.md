# Music Tool Bot

Music Tool Bot is the ultimate bot for managing your music files effortlessly! 🎵✨. Check it out here:
[@MusicToolBot](https://t.me/MusicToolBot)

Supports 2 languages for now: **English** and **Persian**. ([Add more if you want](#contribution))

### Requirements to run this bot

1. Python 3.8 or higher (Preferably)
2. `ffmpeg`
3. `venv`
4. Optionally you can install `pm2` (globally) which is a Node.js module to manage processes. Since `pm2` can also
   manage Python processes, I use it to run the bot in production. No Node.js/JavaScript knowledge is required. Just
   install `pm2` and run convenient script runners using `pipenv`. If you want to run the bot using other process
   managers, that's fine.

---

### Project setup

0. **Register for a Telegram Bot**:<br />
   Register a new bot at [Bot Father](https://t.me/BotFather) and get a bot token.

1. **Clone this repo:**<br />
   Run `git clone https://github.com/amirhoseinsalimi/music-tool-bot.git music-tool-bot && cd music-tool-bot`

2. **Fire up your venv shell:**<br />
    - Run `python3 -m venv venv` to create a virtual environment
    - Run `source venv/bin/activate` to activate the virtual environment
    - Run `pip install pipenv` to install pipenv. If you get an error regarding building the `wheel` library while
      installing packages, you can install python v3.11.x.

3. **Install dependencies:**<br />
   Run `pipenv install -d`

4. **Setup environment variables:**<br />
   Run `cp .env.example .env`. Then put your credentials there:
   | Field                      | Type  | Description                                                                 |
   | ---------------------------| ----- |---------------------------------------------------------------------------- |
   | OWNER_USER_ID              | `int` | The user ID of the owner of the bot (YOU). This user can add/delete admins. |
   | BOT_NAME                   | `str` | The name of the bot                                                         |
   | BOT_USERNAME               | `str` | The username of the bot. This username is sent as signature in captions.    |
   | BOT_TOKEN                  | `str` | The bot token you grabbed from @BotFather                                   |
   | DB_NAME                    | `str` | Database name. Read the next step for more information.                     |
   | BTC_WALLET_ADDRESS         | `str` | BTC wallet address to receive donations.                                    |
   | ETH_WALLET_ADDRESS         | `str` | ETH wallet address to receive donations.                                    |
   | TRX_WALLET_ADDRESS         | `str` | TRX wallet address to receive donations.                                    |
   | USDT_TRC20_WALLET_ADDRESS  | `str` | USDT (TRC20) wallet address to receive donations.                           |
   | USDT_ERC20_WALLET_ADDRESS  | `str` | USDT (ERC20) wallet address to receive donations.                           |
   | SHIBA_BEP20_WALLET_ADDRESS | `str` | SHIBA (BEP20) wallet address to receive donations.                          |
   | SHIBA_ERC20_WALLET_ADDRESS | `str` | SHIBA (ERC20) wallet address to receive donations.                          |
   | DOGE_WALLET_ADDRESS        | `str` | DOGE wallet address to receive donations.                                   |
   | ZARIN_LINK_ADDRESS         | `str` | ZarinLink address to receive donations.                                     |
   
5. **Set up the database:**<br />
   This bot persists the IDs of users and admins in a SQLite database. So you need to create a database followed by
   running migrations:<br />
   `pipenv run db:migrate`.<br />
   Then run seeds to populate the `admins` table with an owner-level
   access:<br />
   `pipenv run db:seed`.

6. **Run the bot**<br />
   a. Start the bot `pipenv run start`<br />
   b. Restart the bot `pipenv run restart`<br /><br />

See below for all possible commands:
| Command `pipenv run <command>`   | Description                                                                                |
| ------------------------------   | ------------------------------------------------------------------------------------------ |
| `dev`                            | Start the bot for development with hot reload thanks to `jurigged`                         |
| `start`                          | Start the bot for production using `pm2` module. Creates a process called `music-tool-bot` |
| `restart`                        | Restarts the bot process with the name `music-tool-bot`                                    |
| `stop`                           | Stops the bot process with the name `music-tool-bot`                                       |
| `db:migrate`                     | Run migrations                                                                             |
| `db:refresh`                     | Rollback all migration and re-run them (Use with caution)                                  |
| `db:status`                      | Print the status of migrations                                                             |
| `db:seed`                        | Run seeds to create a user with owner privileges                                           |
| `test`                           | Run tests (Not implemented yet)                                                            |
| `t`                              | Alias for `test` command                                                                   |

---

# Contribution

In the beginning, I had written this bot in JavaScript, but due to a lack of quality packages, it was full of bugs. Then
I decided to learn Python and thought: **Why not re-write @MusicToolBot in Python?** And then I began to revive the
project. <br />

This tiny bot is my first practical Python project. I tried to learn Python along with coding, so I could better wrap my
head around the syntax and the built-in functionality of the language. However, as a novice Python developer, I know
this bot can be written in a more smart way with better code structure. So, if you know Python, I would really
appreciate
any help to make this kid better. My main concern is the application structure, but please feel free to create PRs, open
discussions and make small fixes (like typos). In addition, I have some plans and features for this bot, you can find
them on the
[issue board](https://github.com/amirhoseinsalimi/music-tool-bot/issues). Also, I'd be very appreciated if you can
translate the bot to your language.
