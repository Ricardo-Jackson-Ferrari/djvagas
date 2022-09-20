from rolepermissions.roles import AbstractUserRole

manage_job = 'create_job'
manage_account = 'manage_account'
create_manage = 'create_manage'


class Company(AbstractUserRole):
    available_permissions = {
        manage_job: True,
        manage_account: True,
        create_manage: True,
    }


class CompanyManage(AbstractUserRole):
    available_permissions = {
        manage_job: True,
    }


apply_job = 'apply_job'


class Candidate(AbstractUserRole):
    available_permissions = {
        apply_job: True,
    }
