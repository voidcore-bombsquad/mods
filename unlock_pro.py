# Released under the MIT License. See LICENSE for details.
#

from ba import app, Plugin


def main() -> None:
    app.accounts.have_pro = lambda: True
    app.accounts.on_app_launch()


# ba_meta require api 6
# ba_meta export plugin
class ProVersion(Plugin):
    def on_app_launch(self) -> None:
        main()