#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

#html format
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: blue;
        }
    </style>
</head>
<body>
    <h1>User Signup
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

class Index(webapp2.RequestHandler):
    def get(self):
        edit_header = "<h3>User Signup</h3>"

        add_form = """
        <form action="/output" method="post">
          <table>
          <tr>
            <td class="label">
                  Username
            </td>
            <td>
                  <input type="text" name="username" value="">
                </td>
                </tr>

        <tr>
            <td class="label">
                Password
                </td>
                <td>
                <input type="password" name="password" value="">
                </td>
            </tr>
            <tr>
            <td class="label">
                Verify Password
                </td>
                <td>
                <input type="password" name="verify" value="">
                </td>
        </tr>
            <tr>
            <td class="label">
             Email (optional)
             </td>
             <td>
          <input type="text" name="email" value="">
          </td>
          </tr>
        </table>
        <input type="submit">
     </form>
        """


# if we have an error, make a <p> to display it
        #error = self.request.get("error")
        #error_element = "<p class='error'>" + error + "</p>" if error else ""

#combine all pieces
        response = page_header + "<p>" + add_form + "</p>" + page_footer
        self.response.write(response)

class Output(webapp2.RequestHandler):
#rotates text based user input
#requests coming into '/add'
    def post(self):
# look inside the request to figure out what the user typed
        user_form = self.request.get("username")
        pass_form = self.request.get("password")
        verify_form = self.request.get("verify")
        email_form = self.request.get("email")
        #new_post = self.request.get("username")

        #have_error = False
        #username = self.request.get('username')
        #password = self.request.get('password')
        #verify = self.request.get('verify')
        #email = self.request.get('email')

        if new_post != "":
            error = "Please enter valid text."
            error_escaped = cgi.escape(error, quote=True)


        new_post_element = "<strong>" + cgi.escape(new_post) + "</strong>"
        sentence = new_post_element + " has been submitted!"
        response = page_header + "<p>" + sentence + "</p>" + page_footer
        self.response.write(response)


app = webapp2.WSGIApplication([
    ('/', Index),
    ('/', Output)
], debug=True)
