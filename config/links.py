"""Хранение ссылок."""

class Links:

    HOST = "https://opensource-demo.orangehrmlive.com/web/index.php/"

    LOGIN_PAGE = f"{HOST}auth/login"

    ADMIN_PAGE = f"{HOST}admin/viewSystemUsers"
    PIM_PAGE = f"{HOST}pim/viewEmployeeList"
    LEAVE_PAGE = f"{HOST}leave/viewLeaveList"
    TIME_PAGE = f"{HOST}time/viewEmployeeTimesheet"
    RECRUITMENT_PAGE = f"{HOST}recruitment/viewCandidates"
    MY_INFO_PAGE = f"{HOST}pim/viewPersonalDetails/empNumber/7"
    PERFORMANCE_PAGE = f"{HOST}performance/searchEvaluatePerformanceReview"
    DASHBOARD_PAGE = f"{HOST}dashboard/index" # main page
    DIRECTORY_PAGE = f"{HOST}directory/viewDirectory"
    MAINTENANCE_PAGE = f"{HOST}maintenance/purgeEmployee"
    CLAIM_PAGE = f"{HOST}claim/viewAssignClaim"
    BUZZ_PAGE = f"{HOST}buzz/viewBuzz"

