#   THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
#   FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY APPDYNAMICS.

################################################################################
# 2018-10-131 - 1 - Tom Batchelor - Initial release, basic PyPy Bindings using CFFI
#
#
################################################################################

from cffi import FFI
ffibuilder = FFI()

# cdef() expects a string listing the C types, functions and
# globals needed from Python. The string follows the C syntax.
ffibuilder.cdef("""
    typedef void* appd_bt_handle;
    typedef void* appd_exitcall_handle;
    typedef void* appd_frame_handle;

    struct appd_config;
    struct appd_context_config;

    enum appd_config_log_level
    {
      APPD_LOG_LEVEL_TRACE,
      APPD_LOG_LEVEL_DEBUG,
      APPD_LOG_LEVEL_INFO,
      APPD_LOG_LEVEL_WARN,
      APPD_LOG_LEVEL_ERROR,
      APPD_LOG_LEVEL_FATAL
    };

    struct appd_config* appd_config_init();

    void appd_config_set_app_name(struct appd_config* cfg, const char* app);

    void appd_config_set_tier_name(struct appd_config* cfg, const char* tier);

    void appd_config_set_node_name(struct appd_config* cfg, const char* node);

    void appd_config_set_controller_host(struct appd_config* cfg, const char* host);
    void appd_context_config_set_controller_host(struct appd_context_config* context_cfg, const char* host);

    void appd_config_set_controller_port(struct appd_config* cfg, const unsigned short port);
    void appd_context_config_set_controller_port(struct appd_context_config* context_cfg, const unsigned short port);

    void appd_config_set_controller_account(struct appd_config* cfg, const char* acct);
    void appd_context_config_set_controller_account(struct appd_context_config* context_cfg, const char* acct);

    void appd_config_set_controller_access_key(struct appd_config* cfg, const char* key);
    void appd_context_config_set_controller_access_key(struct appd_context_config* context_cfg, const char* key);

    void appd_config_set_controller_use_ssl(struct appd_config* cfg, const unsigned int ssl);
    void appd_context_config_set_controller_use_ssl(struct appd_context_config* context_cfg, unsigned int ssl);

    void appd_config_set_controller_http_proxy_host(struct appd_config* cfg, const char* host);
    void appd_context_config_set_controller_http_proxy_host(struct appd_context_config* context_cfg, const char* host);

    void appd_config_set_controller_http_proxy_port(struct appd_config* cfg, const unsigned short port);
    void appd_context_config_set_controller_http_proxy_port(struct appd_context_config* context_cfg, const unsigned short port);

    void appd_config_set_controller_http_proxy_username(struct appd_config* cfg, const char* user);
    void appd_context_config_set_controller_http_proxy_username(struct appd_context_config* context_cfg, const char* user);

    void appd_config_set_controller_http_proxy_password(struct appd_config* cfg, const char* pwd);
    void appd_context_config_set_controller_http_proxy_password(struct appd_context_config* context_cfg, const char* pwd);

    void appd_config_set_controller_http_proxy_password_file(struct appd_config* cfg, const char* file);
    void appd_context_config_set_controller_http_proxy_password_file(struct appd_context_config* context_cfg, const char* file);

    void appd_config_set_controller_certificate_file(struct appd_config* cfg, const char* file);
    void appd_context_config_set_controller_certificate_file(struct appd_context_config* context_cfg, const char* file);

    void appd_config_set_controller_certificate_dir(struct appd_config* cfg, const char* dir);
    void appd_context_config_set_controller_certificate_dir(struct appd_context_config* context_cfg, const char* dir);

    void appd_config_set_logging_min_level(struct appd_config* cfg, enum appd_config_log_level lvl);

    void appd_config_set_logging_log_dir(struct appd_config* cfg, const char* dir);

    void appd_config_set_logging_max_num_files(struct appd_config* cfg, const unsigned int num);

    void appd_config_set_logging_max_file_size_bytes(struct appd_config* cfg, const unsigned int size);

    void appd_config_set_init_timeout_ms(struct appd_config* cfg, const int time);

    void appd_config_set_flush_metrics_on_shutdown(struct appd_config* cfg, int enable);

    void appd_config_getenv(struct appd_config* cfg, const char* prefix);

    struct appd_context_config* appd_context_config_init(const char* context);

    void appd_context_config_set_app_name(struct appd_context_config* context_cfg, const char* app);

    void appd_context_config_set_tier_name(struct appd_context_config* context_cfg, const char* tier);

    void appd_context_config_set_node_name(struct appd_context_config* context_cfg, const char* node);

    int appd_sdk_add_app_context(struct appd_context_config* context_cfg);

    int appd_sdk_init(const struct appd_config* config);

    void appd_backend_declare(const char* type, const char* unregistered_name);

    int appd_backend_set_identifying_property(const char* backend, const char* key, const char* value);

    int appd_backend_prevent_agent_resolution(const char* backend);

    int appd_backend_add(const char* backend);

    appd_bt_handle appd_bt_begin(const char* name, const char* correlation_header);

    appd_bt_handle appd_bt_begin_with_app_context(const char* context, const char* name, const char* correlation_header);

    void appd_bt_store(appd_bt_handle bt, const char* guid);

    appd_bt_handle appd_bt_get(const char* guid);

    enum appd_error_level
    {
      APPD_LEVEL_NOTICE,
      APPD_LEVEL_WARNING,
      APPD_LEVEL_ERROR
    };

    void appd_bt_add_error(appd_bt_handle bt, enum appd_error_level level, const char* message, int mark_bt_as_error);

    char appd_bt_is_snapshotting(appd_bt_handle bt);

    void appd_bt_add_user_data(appd_bt_handle bt, const char* key, const char* value);

    void appd_bt_set_url(appd_bt_handle bt, const char* url);

    void appd_bt_end(appd_bt_handle bt);

    appd_exitcall_handle appd_exitcall_begin(appd_bt_handle bt, const char* backend);

    void appd_exitcall_store(appd_exitcall_handle exitcall, const char* guid);

    appd_exitcall_handle appd_exitcall_get(const char* guid);

    int appd_exitcall_set_details(appd_exitcall_handle exitcall, const char* details);

    const char* appd_exitcall_get_correlation_header(appd_exitcall_handle exitcall);

    void appd_exitcall_add_error(appd_exitcall_handle exitcall, enum appd_error_level level, const char* message, int mark_bt_as_error);

    void appd_exitcall_end(appd_exitcall_handle exitcall);

    enum appd_time_rollup_type
    {
      APPD_TIMEROLLUP_TYPE_AVERAGE = 1,
      APPD_TIMEROLLUP_TYPE_SUM,
      APPD_TIMEROLLUP_TYPE_CURRENT
    };

    enum appd_cluster_rollup_type
    {
      APPD_CLUSTERROLLUP_TYPE_INDIVIDUAL = 1,
      APPD_CLUSTERROLLUP_TYPE_COLLECTIVE
    };

    enum appd_hole_handling_type
    {
      APPD_HOLEHANDLING_TYPE_RATE_COUNTER = 1,
      APPD_HOLEHANDLING_TYPE_REGULAR_COUNTER
    };

    void appd_custom_metric_add(const char* application_context, const char* metric_path, enum appd_time_rollup_type time_rollup_type, enum appd_cluster_rollup_type cluster_rollup_type, enum appd_hole_handling_type hole_handling_type);

    void appd_custom_metric_report(const char* application_context, const char* metric_path, long value);

    enum appd_frame_type
    {
      APPD_FRAME_TYPE_CPP = 1
    };

    appd_frame_handle appd_frame_begin(appd_bt_handle bt, enum appd_frame_type frame_type, const char* class_name, const char* method_name, const char* file, unsigned int line_number);

    void appd_frame_end(appd_bt_handle bt, appd_frame_handle frame);

    void appd_sdk_term();
""")

# This describes the extension module "_pi_cffi" to produce.
ffibuilder.set_source("_pi_cffi",
"""
     #include "appdynamics.h"   // the C header of the library
""",
     libraries=['appdynamics'])   # library name, for the linker

if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
