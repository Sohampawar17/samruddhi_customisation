app_name = "samruddhi_customisation"
app_title = "Samruddhi Customisation"
app_publisher = "Quantbit Technologies"
app_description = "Samruddhi customisation"
app_email = "contact@erpdata.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/samruddhi_customisation/css/samruddhi_customisation.css"
# app_include_js = "/assets/samruddhi_customisation/js/samruddhi_customisation.js"

# include js, css files in header of web template
# web_include_css = "/assets/samruddhi_customisation/css/samruddhi_customisation.css"
# web_include_js = "/assets/samruddhi_customisation/js/samruddhi_customisation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "samruddhi_customisation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "samruddhi_customisation/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "samruddhi_customisation.utils.jinja_methods",
# 	"filters": "samruddhi_customisation.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "samruddhi_customisation.install.before_install"
# after_install = "samruddhi_customisation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "samruddhi_customisation.uninstall.before_uninstall"
# after_uninstall = "samruddhi_customisation.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "samruddhi_customisation.utils.before_app_install"
# after_app_install = "samruddhi_customisation.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "samruddhi_customisation.utils.before_app_uninstall"
# after_app_uninstall = "samruddhi_customisation.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "samruddhi_customisation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"samruddhi_customisation.tasks.all"
# 	],
# 	"daily": [
# 		"samruddhi_customisation.tasks.daily"
# 	],
# 	"hourly": [
# 		"samruddhi_customisation.tasks.hourly"
# 	],
# 	"weekly": [
# 		"samruddhi_customisation.tasks.weekly"
# 	],
# 	"monthly": [
# 		"samruddhi_customisation.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "samruddhi_customisation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "samruddhi_customisation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "samruddhi_customisation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["samruddhi_customisation.utils.before_request"]
# after_request = ["samruddhi_customisation.utils.after_request"]

# Job Events
# ----------
# before_job = ["samruddhi_customisation.utils.before_job"]
# after_job = ["samruddhi_customisation.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"samruddhi_customisation.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

