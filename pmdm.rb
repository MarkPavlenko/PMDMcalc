class Pmdm < Formula
    desc "PMDM Calculator"
    homepage "https://github.com/yourusername/pmdm"
    url "https://github.com/yourusername/pmdm/archive/v1.0.tar.gz"
    sha256 "checksum_of_your_tarball"
  
    def install
      bin.install "pmdm.py" => "pmdm"
    end
  
    test do
      assert_equal "PMDM version 1.0", shell_output("#{bin}/pmdm --version").strip
    end
  end
  