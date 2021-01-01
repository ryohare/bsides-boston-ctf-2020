package main

import (
	"crypto/rand"
	"crypto/rsa"
	"fmt"
	"math/big"
)

func main() {
	N := "25731230666969714678742709822906857643182953294318637715279924877135973526525329394086786215919632231591232627827318259655595846938846578523320336897042185209221085492463582835874594388048142193443461443069777754165578705365515179654161434989884904694750406175168414907813720504165651049056839904539466298026072999963728843595610866147631362818671559173632008484641003104012485406896618153192212040445556962648070681677972635087537728956426202327950035197070607426092169365550385898554130903938977543053270297116818102810102826147882406131179979695011992859082480826759440109269421115917806600858227857451301402482393"
	E := 65537
	bigN := new(big.Int)
	_, ok := bigN.SetString(N, 16)
	if !ok {
		panic("failed to parse")
	}
	pub := rsa.PublicKey{
		N: bigN,
		E: E,
	}

	msg := []byte("test message")
	rng := rand.Reader
	// label := []byte("orders")

	// ct, err := rsa.EncryptOAEP(sha256.New(), rng, &pub, msg, label)
	ct, err := rsa.EncryptPKCS1v15(rng, &pub, msg)

	if err != nil {
		panic("failed to encrypt")
	}
	for _, v := range ct {
		fmt.Print(v)
	}
	fmt.Println()
}
