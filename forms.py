from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
  first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
  last_name = StringField('Last name', validators=[DataRequired("Please enter your last name.")])
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password."), Length(min=6, message="Passwords must be 6 characters or more.")])
  submit = SubmitField('Sign up')

class LoginForm(Form):
  email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
  password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
  submit = SubmitField("Sign in")

'''
# Create a list of Tuples
'''
def createTypes(types, delimiter=';'):
    segrated = types.split(delimiter)

    final_types = list()
    for index,item in enumerate(segrated):
        tuple = item.strip(), item.strip()
        final_types.append(tuple)
    return final_types

class NewProductRequestForm(Form):
    __technology_types = [ ('ATG' , 'ATG'),
                         ('ATG4', 'ATG4'),
                         ('KU', 'KU'),
                         ('2KU', '2KU')
                    ]


    productName = StringField('Product Name', validators=[DataRequired("Please enter the data.")], render_kw={"placeholder": "example: CAS_CREW, SIVER"})

    region_types = createTypes('Domestic;International;Both')
    region = SelectField('Region', validators=[DataRequired("Please enter the data.")], choices=region_types)

    technology_types = createTypes('ATG;ATG4;KU;2KU')
    technology = SelectField('Technology', validators=[DataRequired("Please enter the data.")], choices=technology_types)

    usersCategory_types = createTypes('PAX;CAS;UNPAID;GGV;FAM;3PP;TMO;EAPAKA;ALL')
    usersCategory = SelectField('Users Category', validators=[DataRequired("Please enter the data.")], choices=usersCategory_types)

    environment_types = createTypes('PROD;LAB')
    environment = SelectField('Environment', validators=[DataRequired("Please enter the data.")], choices=environment_types)

    serviceCodeType = StringField('Service Code/Type', validators=[DataRequired("Please enter the data.")], render_kw={"placeholder": "example: WIFI,WIFI14,PG1AG"})
    dpiParameters = StringField('Service Code/Type', validators=[DataRequired("Please enter the data.")], render_kw={"placeholder": "example: WIFI,WIFI14,PG1AG"})

    dpi_fl_rate_limit_types = createTypes('1000;12;13000;16;20;22000;24;3000;32;400;4000;500;5000;6000;')
    dpi_fl_rate_limit = SelectField('FL(Download) Rate Limit Pre-VC (Kbps)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_fl_rate_limit_types)

    dpi_rl_rate_limit_types = createTypes('1000;12;16;20;24;300;32;400;500;600;6000')
    dpi_rl_rate_limit = SelectField('RL(Upload) Rate Limit Pre-VC (Kbps)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_rl_rate_limit_types)

    dpi_fl_volume_control_types = createTypes('1000;200;2000;250;400;50;600')
    dpi_fl_volume_control = SelectField('FL(Download) Volume Control/Threshold (MB)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_fl_volume_control_types)

    dpi_rl_volume_control_types = createTypes('100;200;400;50')
    dpi_rl_volume_control = SelectField('RL(Upload) Volume Control/Threshold (MB)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_rl_volume_control_types)

    dpi_fl_rate_limit_post_types = createTypes('50;120;100;360;240;35;150;10;90;300;60;30')
    dpi_fl_rate_limit_post = SelectField('FL(Download) Rate Limit Post-VC (Kbps)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_fl_rate_limit_post_types)

    dpi_rl_rate_limit_post_types = createTypes('15;10;20;360;15;25;60;5;50;30;120')
    dpi_rl_rate_limit_post = SelectField('RL(Upload) Rate Limit Post-VC (Kbps)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_rl_rate_limit_post_types)


    dpi_fl_voip_rate_limit_types = createTypes('12;16;20;24;32;')
    dpi_fl_voip_rate_limit = SelectField('FL(Download) VOIP Rate Limit (Kbps)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_fl_voip_rate_limit_types)


    dpi_rl_voip_rate_limit_types = createTypes('12;16;20;24;32;')
    dpi_rl_voip_rate_limit = SelectField('RL(Upload) VOIP Rate Limit (Kbps)',
                                    validators=[DataRequired("Please enter the data.")],
                                    choices=dpi_rl_voip_rate_limit_types)

    dpi_blocking_feature_types = createTypes('BlacklistURL; BlockApplications; BlockCategories; blockipports; new; none')
    dpi_blocking_feature = SelectField('Blocking Feature',
                                        validators=[DataRequired("Please enter the data.")],
                                        choices=dpi_blocking_feature_types)

    dpi_shaping_feature_types = createTypes('ShapeApplications;shapeipports')
    dpi_shaping_feature= SelectField('Shaping Feature',
                                        validators=[DataRequired("Please enter the data.")],
                                        choices=dpi_shaping_feature_types)

    dpi_allow_feature_types = createTypes('whitelists;urls;Whitelisturlspeedtest')
    dpi_allow_feature = SelectField('Allow Feature',
                                        validators=[DataRequired("Please enter the data.")],
                                        choices=dpi_allow_feature_types)

    dpi_content_filter_types = createTypes('xxx sites')
    dpi_content_filter = SelectField('Content-Filter',
                                        validators=[DataRequired("Please enter the data.")],
                                        choices=dpi_content_filter_types)

    dpi_msg_whitelist_types = createTypes('whitelist_cas; whitelist_msg')
    dpi_msg_whitelist = SelectField('MSG White List Version',
                                        validators=[DataRequired("Please enter the data.")],
                                        choices=dpi_msg_whitelist_types)

    dpi_big_sockets_types = createTypes('yes;numbers')
    dpi_big_sockets = SelectField('Bigsockets',
                                        validators=[DataRequired("Please enter the data.")],
                                        choices=dpi_big_sockets_types)

    dpi_acpu_release = StringField('ACPU Release', validators=[DataRequired("Please enter the data.")])

    policyName = StringField('Policy Name', validators=[DataRequired("Please enter the data.")], render_kw={"placeholder": "test"})
    submit = SubmitField("Submit Request")

