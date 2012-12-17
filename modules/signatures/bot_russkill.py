# Copyright (C) 2012 JoseMi Holguin (@j0sm1)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class Ruskill(Signature):
    name = "bot_russkill"
    description = "Creates known Ruskill mutexes"
    severity = 3
    alert = True
    categories = ["bot", "ddos"]
    authors = ["JoseMi Holguin"]
    maximum = "0.4.2"

    def run(self, results):
        for mutex in results["behavior"]["summary"]["mutexes"]:
            if mutex == "FvLQ49IlzIyLjj6m":
                self.data.append({"mutex" : mutex})
                return True

        return False
