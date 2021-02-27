# Directory locations:
BININSTALLROOTDIR="/etc/init.d"
BASEINSTALLDIR_OPT="/opt/google"
BASEINSTALLDIR_ETC="/etc/opt/google"
BASEINSTALLDIR_VAR="/var/opt/google"

# Derived directories:
SYSTEMRC="$BASEINSTALLDIR_ETC/systemrc"
MIN_ASSET_ROOT_VOLUME_SIZE_IN_KB=1048576

# Configuration values:
ASSET_ROOT="/gevol/assets"
SOURCE_VOLUME="/gevol/src"

# Commands:
NEWLINECLEANER="sed -e s:\\n::g"

if [ -f /sbin/chkconfig ]; then
    # Use the Red Hat tool for managing services:
    add_service()
    {
        local SERVICE_NAME="$1"

        /sbin/chkconfig --add "$SERVICE_NAME"
    }

    remove_service()
    {
        local SERVICE_NAME="$1"

        /sbin/chkconfig --del "$SERVICE_NAME"
    }
elif [ -f /usr/sbin/update-rc.d ]; then
    # Use the Debian tool for managing services:
    add_service()
    {
        local SERVICE_NAME="$1"

        # For Ubuntu 14:
        /usr/sbin/update-rc.d "$SERVICE_NAME" start 90 2 3 4 5 . stop 10 0 1 6 .
    }

    remove_service()
    {
        local SERVICE_NAME="$1"

        /usr/sbin/update-rc.d -f "$SERVICE_NAME" remove
    }
else
    echo "Error: Unable to find a command for adding and removing services." >&2
    exit 1
fi


load_systemrc_config()
{
    local VALUE

    if [ -f "$SYSTEMRC" ]; then
        # Read configuration:
        VALUE=$(xml_file_get_xpath "$SYSTEMRC" "//Systemrc/assetroot/text()")
        [ -z "$VALUE" ] || ASSET_ROOT="$VALUE"

        VALUE=$(xml_file_get_xpath "$SYSTEMRC" "//Systemrc/fusionUsername/text()")
        [ -z "$VALUE" ] || GEFUSIONUSER="$VALUE"

        VALUE=$(xml_file_get_xpath "$SYSTEMRC" "//Systemrc/userGroupname/text()")
        [ -z "$VALUE" ] || GEGROUP="$VALUE"
    fi
}

xml_file_get_xpath()
{
    local FILE="$1"
    local XPATH="$2"

    # Warning: `xmllint --noent` doesn't recognize named entities like
    # "&lt;" and "&gt;":
    echo "cat $XPATH" | xmllint --noent --nocdata --shell "$FILE" |
    # Skip the first and the last line:
        tail -n +2 | head -n -1
}
