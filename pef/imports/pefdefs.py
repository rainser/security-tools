# Definitions for pef.py

# exploitable functions
exploitableFunctions = [
    "system(",
    "exec(",
    "popen(",
    "pcntl_exec(",
    "eval(",
    "preg_replace(",
    "create_function(",
    "include(",
    "require(",
    "passthru(",
    "shell_exec(",
    "popen(",
    "proc_open(",
    "pcntl_exec(",
    "extract(",
    "parse_str(",
    "putenv(",
    "ini_set(",
    "mail(",
    "header(",
    "unserialize(",
    "apache_child_terminate(",
    "apache_get_modules(",
    "assert(",
    "call_user_func(",
    "call_user_func_array(",
    "ereg_replace(",
    "eregi_replace(",
    "mb_ereg_replace(",
    "mb_eregi_replace(",
    "virtual",
    "readfile(",
    "file_get_contents(",
    "show_source(",
    "fopen(",
    "file(",
    "fpassthru(",
    "gzopen(",
    "gzfile(",
    "gzpassthru(",
    "readgzfile(",
    "mssql_query(",
    "move_uploaded_file(",
    "echo",
    "print(",
    "printf(",
    "xpath(",
    "ldap_search(",
    "header(",
    "http_redirect",
    "HttpMessage::setResponseCode",
    "HttpMessage::setHeaders",
    "HttpRequest::setHeaders",
    "sqlite_",
    "pg_",
    "mysql_",
    "mysqli_",
    "apache_note(",
    "apache_setenv(",
    "define_syslog_variables(",
    "disk_free_space(",
    "disk_total_space(",
    "diskfreespace(",
    "dl(",
    "escapeshellarg(",
    "escapeshellcmd(",
    "exec(",
    "extract(",
    "get_cfg_var(",
    "get_current_user(",
    "getcwd(",
    "getenv(",
    "getlastmo(",
    "getmygid(",
    "getmyinode(",
    "getmypid(",
    "getmyuid(",
    "ini_restore(",
    "ini_set(",
    "passthru(",
    "pcntl_alarm(",
    "pcntl_exec(",
    "pcntl_fork(",
    "pcntl_get_last_error(",
    "pcntl_getpriority(",
    "pcntl_setpriority(",
    "pcntl_signal(",
    "pcntl_signal_dispatch(",
    "pcntl_sigprocmask(",
    "pcntl_sigtimedwait(",
    "pcntl_sigwaitinfo(",
    "pcntl_strerrorp(",
    "pcntl_wait(",
    "pcntl_waitpid(",
    "pcntl_wexitstatus(",
    "pcntl_wifexited(",
    "pcntl_wifsignaled(",
    "pcntl_wifstopped(",
    "pcntl_wstopsig(",
    "pcntl_wtermsig(",
    "php_uname(",
    "phpinfo(",
    "popen(",
    "posix_getlogin(",
    "posix_getpwuid(",
    "posix_kill(",
    "posix_mkfifo(",
    "posix_setpgid(",
    "posix_setsid(",
    "posix_setuid(",
    "posix_ttyname(",
    "posix_uname(",
    "posixc(",
    "proc_close(",
    "proc_get_status(",
    "proc_nice(",
    "proc_open(",
    "proc_terminate(",
    "ps_aux(",
    "putenv(",
    "readlink(",
    "runkit_function_rename(",
    "show_source(",
    "symlink(",
    "syslog(",
]

# dangerous global(s)
globalVars = [
    "$_POST",
    "$_GET",
    "$_COOKIE",
    "$_REQUEST",
    "$_SERVER"
]

# dangerous patterns - LFI/RFI
fileInclude = [
    "include($_GET",
    "require($_GET",
    "include_once($_GET",
    "require_once($_GET",
    "include($_REQUEST",
    "require($_REQUEST",
    "include_once($_REQUEST",
    "require_once($_REQUEST"
]

# reflected properties which might leads to eg. XSS
reflectedProperties = [
    "$_SERVER[\"PHP_SELF\"]",
    "$_SERVER[\"SERVER_ADDR\"]",
    "$_SERVER[\"SERVER_NAME\"]",
    "$_SERVER[\"REMOTE_ADDR\"]",
    "$_SERVER[\"REMOTE_HOST\"]",
    "$_SERVER[\"REQUEST_URI\"]",
    "$_SERVER[\"HTTP_USER_AGENT\"]"
]
