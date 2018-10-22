# Snippet configuration example app

This application illustrates the use of Optimizely X Full Stack to configure the Optimizely X Web snippet on a simple web page.

## Repository structure

Here's a description of the important files in this repository:

        snippet-config/application.py  # python webapp which uses Full Stack to render
                                       # the Optimizely Web snippet in the HTML response

        snippet-config/optimizely_config_manager.py     # A simple container class for the
                                                        # Optimizely instance used by application.py

        snippet-config/datafile.json    # A local copy of the Full Stack project datafile
                                        # application.py is configured to read from this file
                                        # rather than directly from cdn.optimizely.com

        snippet-config/update_datafile.sh   # A shell script that updates /datafile.json with
                                            # the contents of the appropriate datafile on
                                            # cdn.optimizely.com

        snippet-config/templates/index.html     # a flask template for a simple web page, rendered by
                                                # application.py

        snippet-config/templates/optimizely_web_snippet.html    # a flask template for the Optimizely
                                                                # Web snippet

## Deploying the application

1. Create and run a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
2. Install requirements: `pip install -r requirements.txt`
3. Run the application `python application.py` (be sure the virtualenv is running)
4. You’re all set. To try this with your own Optimizely projects, modify `FULL_STACK_PROJECT_ID` and `WEB_PROJECT_ID` in `application.py`.

Once you're up and running, you can load the page via

      http://localhost:4001/

## Updating the local Full Stack datafile

`application.py` is configured to load the Full Stack datafile from `./datafile.json`. To refresh the contents of this file and update your running app, complete the following:

1. run `./update_datafile.sh <YOUR SDK KEY>` using your [SDK Key](https://help.optimizely.com/Set_Up_Optimizely/Access_the_datafile_for_a_Full_Stack_project)
2. load `http://localhost:4001/refresh` in your browser.

After making changes in your Full Stack project, you may need to wait a minute for your changes to propagate to Optimizely's CDN.  To ensure that your changes are correctly loaded, double-check that the revision number shown on `http://localhost:4001/refresh` matches the revision number shown in your Full Stack project settings.

## The Snippet Configuration Full Stack Project

Here's a rough schema for the "Snippet Configuration" Full Stack project this application depends on:

      Full Stack "Snippet Configuration" Project
        Feature: snippet_config
          Variable: snippet_url (default value: "https://cdn.optimizely.com/js/11903751716.js")
          Variable: is_snippet_synchronous (default value: True)

![](images/snippet_config.png)

