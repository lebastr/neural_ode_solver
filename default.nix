{ pkgs ? import <nixpkgs> {}
, stdenv ? pkgs.stdenv
} :

let
 self = pkgs.python36Packages;
 tensorboardX = self.callPackage ./tensorboardX.nix {};
 pythonEnv = (pkgs.python3.withPackages
  (ps: with ps;
  [ ipython
      jupyter
      matplotlib
      numpy
#      jetbrains.pycharm-community
      pyqt5
      python
      pytorchWithoutCuda
      tensorboardX
      tqdm
    ]));

python_env_link_dir = "python-env";

shellHook = ''
if [ -d ${python_env_link_dir} ]
then
  echo "Remove old link: ${python_env_link_dir}"
  rm ${python_env_link_dir};
fi

echo Create symbolic link ${python_env_link_dir} to ${pythonEnv}
ln -s ${pythonEnv} ${python_env_link_dir}
'';

in { build= pythonEnv;
     shell= pythonEnv.env.overrideAttrs (x: { shellHook = shellHook; });
   }
