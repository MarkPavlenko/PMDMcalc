class Pmdm < Formula
    desc "PMDM Calculator"
    homepage "https://github.com/MarkPavlenko/PMDMcalc"
    url "https://github.com/MarkPavlenko/PMDMcalc.git", :tag => "v1.0"
  
    def install
      bin.install "pmdm.py" => "pmdm"
    end
  
    test do
      system "#{bin}/pmdm", "--version"
    end
  end  