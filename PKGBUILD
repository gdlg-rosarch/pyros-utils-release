# Script generated with Bloom
pkgdesc="ROS - Miscellaneous tools for pyROS"


pkgname='ros-kinetic-pyros-utils'
pkgver='0.1.4_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin-pip>=0.2.0'
'ros-kinetic-catkin>=0.6.18'
'ros-kinetic-pyros-test>=0.0.3'
'ros-kinetic-rosgraph>=1.11.19'
'ros-kinetic-roslaunch>=1.11.19'
'ros-kinetic-roslint>=0.10.0'
'ros-kinetic-rosnode>=1.11.19'
'ros-kinetic-rospy>=1.11.19'
'ros-kinetic-rostest>=1.11.19'
'ros-kinetic-rosunit>=1.11.12'
)

depends=('ros-kinetic-rosgraph>=1.11.19'
'ros-kinetic-roslaunch>=1.11.19'
'ros-kinetic-rospy>=1.11.19'
'ros-kinetic-rostest>=1.11.19'
)

conflicts=()
replaces=()

_dir=pyros_utils
source=()
md5sums=()

prepare() {
    cp -R $startdir/pyros_utils $srcdir/pyros_utils
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

